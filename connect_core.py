from sqlalchemy import MetaData, Table, Column, Integer, String, Text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select
import asyncio

meta = MetaData()

users_table = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=True),
    Column("email", String, nullable=False),
    Column("bio", Text, nullable=False),
)

async def async_main():
    engin = create_async_engine("sqlite+aiomysql:///sample.db", echo=True)

    async with engin.begin() as conn:
        # create database
        await conn.run_sync(meta.create_all)

        # insert data
        await conn.execute(
            users_table.insert(),[
                {'username': 'spongebob', 'email': 'spongebob@test.com', 'bio': 'I live in a pineapple under the sea'},
                {'username': 'peter', 'email': 'peterparker@test.com', 'bio': 'I am spiderman'},
                {'username': 'tony', 'email': 'tonystark@test.com', 'bio': 'I am ironman'},
            ]
        )
    #select data
    async with engin.connect() as conn:
asyncio.run(async_main())