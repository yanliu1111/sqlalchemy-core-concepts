from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List
import asyncio
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
) 
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    bio:Mapped[str] = mapped_column(nullable=False)
    comments:Mapped[List["Comment"]] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f"<User username={self.username} >"

class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="comments")

    def __repr__(self):
        return f"<Comment text={self.comment_text} by {self.user.username}>"

# insert data
async def insert_data(sessionmaker: async_sessionmaker[AsyncSession]):
    async with sessionmaker() as session:
       async with session.begin():
              session.add_all(
                [
                     User(
                          username="spongebob",
                          email="spongebob@test.com",
                          bio="I live in a pineapple under the sea",
                          comments = [
                                Comment(comment_text="I am bob"),
                                Comment(comment_text="I am a sponge"),
                            ]),
                    User(
                          username="peter",
                          email="peterparker@test.com",
                          bio="I am spiderman",
                          comments = [
                              Comment(comment_text="I am peter"),
                              Comment(comment_text="I am spiderman"),
                        ]),
                ])
              
              session.commit()
       
# main is the name of the coroutine
async def async_main():
    
    # create the engine
    engine = create_async_engine("sqlite+aiosqlite:///sample2.db", echo=True)
    # create the session
    session = async_sessionmaker(bind=engine, expire_on_commit=False)

    async with engine.begin() as conn:
        # create database
        # await conn.run_sync(Base.metadata.create_all)
        await insert_data(session)

asyncio.run(async_main())