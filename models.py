from sqlmodel import Field, SQLModel, Relationship, Column, DateTime
from datetime import datetime


class Profile(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    username: str | None

    posts: list["Post"] = Relationship(back_populates="profile")


class Post(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    text: str | None
    favorite_count: int
    retweet_count: int
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    profile_id: str = Field(default=None, foreign_key="profile.id")
    profile: Profile = Relationship(back_populates="posts")

    replies: list["Reply"] = Relationship(back_populates="post")


class Reply(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    text: str

    post_id: str | None = Field(default=None, foreign_key="post.id")
    post: Post = Relationship(back_populates="replies")
