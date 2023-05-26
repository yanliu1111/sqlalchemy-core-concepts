from sqlalchemy import insert
from tables import users_table
from connect import engine

statement = insert(users_table)
with engine.connect() as conn:
    conn.execute(statement, [
        {'name': 'spongebob', 'fullname': 'Spongebob Squarepants'},
        {'name': 'tony', 'fullname': 'Tony Stark'},
    ])
    conn.commit()