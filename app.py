import asyncio
import requests
import uuid
from datetime import datetime
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc
from models import Post, Profile, Reply
from params import Params
from database import Database
from logger import *

scheduler = AsyncIOScheduler(timezone=utc)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Database.create_db_and_tables()
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)


@scheduler.scheduled_job('interval', seconds=1800)
def scrape():
    logger.info('Starting scraping...')
    session = next(Database.get_session())
    profiles = session.exec(select(Profile)).all()

    for i, profile in enumerate(profiles):
        params = Params.params_factory(profile.user_id, '', True)

        tweets = requests.get(
            'https://api.x.com/graphql/TK4W-Bktk8AJk0L1QZnkrg/UserTweets',
            params=params,
            cookies=Params.cookies,
            headers=Params.headers,
        )

        for entry in tweets.json()["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"]:
            try:
                data = entry["content"]["itemContent"]["tweet_results"]["result"]["legacy"]

                full_text = data["full_text"]
                repost = int(data["retweet_count"]) + int(data["quote_count"])
                comments = int(data["reply_count"])
                favorited = int(data["favorite_count"])
                created_at = data["created_at"]

                tweet_id = data["id_str"]

                tweet_params = Params.params_factory('', tweet_id, False)

                reply_data = requests.get(
                    'https://x.com/i/api/graphql/iP4-On5YPLPgO9mjKRb2Gg/TweetDetail',
                    params=tweet_params,
                    cookies=Params.cookies,
                    headers=Params.headers,
                )

                replies = []
                try:
                    r = reply_data.json()[
                        "data"]['threaded_conversation_with_injections_v2']['instructions'][0]['entries'][1:]

                    try:
                        for reply in r:
                            # TODO: might need some processing here to remove the username from the start of the reply
                            reply_text = reply["content"]['items'][0]['item']['itemContent'][
                                'tweet_results']['result']['legacy']['full_text']
                            replies.append(
                                Reply(id=uuid.uuid4(), text=reply_text, post_id=tweet_id))
                    except Exception:
                        pass

                except Exception as ex:
                    logger.info(str(ex))

                post = Post(id=uuid.uuid4(), text=full_text, favorite_count=favorited,
                            retweet_count=repost + comments, created_at=created_at, profile_id=profile.id, replies=replies)

                session.add(post)

                session.commit()
            except Exception as ex:
                logger.error(str(ex))

        print(f"Profile {i} / {len(profiles)}.")


@app.get("/entries/{start_date}/{end_date}")
async def get_entries_by_date_range(
    session: Database.SessionDep,
    start_date: datetime,
    end_date: datetime,
):
    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="Start date must be before end date"
        )

    try:
        entries = next(session).exec(select(Post).filter(
            Post.created_at >= start_date,
            Post.created_at <= end_date
        )).all()
        return entries
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
