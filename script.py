import asyncio
import requests
import uuid
from datetime import datetime
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship, Column, DateTime


class Profile(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)


class Post(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    text: str | None
    favorite_count: int
    retweet_count: int
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    replies: list["Reply"] = Relationship(back_populates="post")


class Reply(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    text: str

    post_id: str | None = Field(default=None, foreign_key="post.id")
    post: Post = Relationship(back_populates="replies")


# connection_string = "postgresql://postgres:password@localhost:5432/ciceroni"
connection_string = "postgresql://postgres:password@88.99.191.92:5432/ciceroni?sslmode=require"


engine = create_engine(connection_string)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

cookies = {
    'guest_id': '173453512022086297',
    'night_mode': '2',
    'guest_id_marketing': 'v1%3A173453512022086297',
    'guest_id_ads': 'v1%3A173453512022086297',
    'gt': '1869401905086017572',
    '_twitter_sess': 'BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74',
    'kdt': 'ngkLSR9ulYSXaDH2GeuoE4Kfoc7D9EXSWsgf6YhY',
    'auth_token': 'b840e6964be1ad7a5761b0cf9bb5bc197be17051',
    'ct0': '46757ba8f4a3bec4bc2ad49cb544c49a5c9787beaa294e7ea7746a67a2326dbad2533c26828b2dba5f31f379b94983b76b776af985a8173ecde7926f4ca78642e3c0462344d31cd583d79a80194a79d2',
    'lang': 'en',
    'twid': 'u%3D1869428382863077376',
    'personalization_id': '"v1_1JanKNmWKX7huSYcTzaVCg=="',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # 'cookie': 'guest_id=173453512022086297; night_mode=2; guest_id_marketing=v1%3A173453512022086297; guest_id_ads=v1%3A173453512022086297; gt=1869401905086017572; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; kdt=ngkLSR9ulYSXaDH2GeuoE4Kfoc7D9EXSWsgf6YhY; auth_token=b840e6964be1ad7a5761b0cf9bb5bc197be17051; ct0=46757ba8f4a3bec4bc2ad49cb544c49a5c9787beaa294e7ea7746a67a2326dbad2533c26828b2dba5f31f379b94983b76b776af985a8173ecde7926f4ca78642e3c0462344d31cd583d79a80194a79d2; lang=en; twid=u%3D1869428382863077376; personalization_id="v1_1JanKNmWKX7huSYcTzaVCg=="',
    'priority': 'u=1, i',
    'referer': 'https://x.com/albinkurti/status/1868981691580047698',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-client-transaction-id': 'pQy1/RVZRRbKL3rD8g/eDb4VsqVI7f0WCQWmw/FLQdYyv2vAUjdMpCISrg/ZkKeud9Y4tqbPAmxTeOdviOG/W8PVT+77pg',
    'x-csrf-token': '46757ba8f4a3bec4bc2ad49cb544c49a5c9787beaa294e7ea7746a67a2326dbad2533c26828b2dba5f31f379b94983b76b776af985a8173ecde7926f4ca78642e3c0462344d31cd583d79a80194a79d2',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}


def params_factory(user_id, tweet_id, is_profile=True):
    params_profile = {
        'variables': f'{{"userId":"{user_id}","count":100,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}}',
        'features': '{"profile_label_improvements_pcf_label_in_post_enabled":false,"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
        'fieldToggles': '{"withArticlePlainText":false}',
    }

    params_tweet = {
        'variables': f'{{"focalTweetId":"{tweet_id}","with_rux_injections":false,"rankingMode":"Relevance","includePromotedContent":true,"withCommunity":true,"withQuickPromoteEligibilityTweetFields":true,"withBirdwatchNotes":true,"withVoice":true}}',
        'features': '{"profile_label_improvements_pcf_label_in_post_enabled":false,"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
        'fieldToggles': '{"withArticleRichContentState":true,"withArticlePlainText":false,"withGrokAnalyze":false,"withDisallowedReplyControls":false}',
    }

    return params_profile if is_profile else params_tweet


def scrape(session: Session):
    print('scraping...')
    profiles = session.exec(select(Profile)).all()

    for profile in profiles:
        test_id = '442918531'
        params = params_factory(test_id, '', True)

        # params = params_factory(profile.user_id, '', True)

        tweets = requests.get(
            'https://api.x.com/graphql/TK4W-Bktk8AJk0L1QZnkrg/UserTweets',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        # print(profile.user_id, tweets.json())

        for entry in tweets.json()["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"]:
            try:
                data = entry["content"]["itemContent"]["tweet_results"]["result"]["legacy"]

                full_text = data["full_text"]
                repost = int(data["retweet_count"]) + int(data["quote_count"])
                comments = int(data["reply_count"])
                favorited = int(data["favorite_count"])
                created_at = data["created_at"]

                tweet_id = data["id_str"]

                tweet_params = params_factory('', tweet_id, False)

                reply_data = requests.get(
                    'https://x.com/i/api/graphql/iP4-On5YPLPgO9mjKRb2Gg/TweetDetail',
                    params=tweet_params,
                    cookies=cookies,
                    headers=headers,
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
                            print(reply_text)
                    except Exception:
                        pass

                except Exception as ex:
                    print(f'Exception Reply: {str(ex)}')

                post = Post(id=uuid.uuid4(), text=full_text, favorite_count=favorited,
                            retweet_count=repost + comments, created_at=created_at, replies=replies)

                session.add(post)

                session.commit()
            except Exception as ex:
                print(f"Exception: {str(ex)}")

            # TODO: Only doing one iteration for development, remove later
            break
    return True


async def task():
    while True:
        try:
            session = next(get_session())
            scrape(session)
        except Exception as e:
            print(f"Task error: {e}")
        finally:
            await asyncio.sleep(30 * 60)


@app.on_event("startup")
async def on_startup():
    create_db_and_tables()
    asyncio.create_task(task())


@app.get("/entries/{start_date}/{end_date}")
async def get_entries_by_date_range(
    session: SessionDep,
    start_date: datetime,
    end_date: datetime,
):
    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="Start date must be before end date"
        )

    try:
        entries = session.exec(select(Post).filter(
            Post.created_at >= start_date,
            Post.created_at <= end_date
        )).all()
        return entries
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
