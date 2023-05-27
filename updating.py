from tables import users_table
from connect import engine
from sqlalchemy import update

statement = update(users_table).where(
    users_table.c.name == 'spongebob').values(name='bob')

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()

    


