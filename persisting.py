from models import User, Comment
# from sqlalchemy.orm import Session
# from connect import engine

# session = Session(bind=engine)
from main import session
user1 = User(
    username="perter",
    email_address="perterparker@test.com",
    comments=[
        Comment(text="I love spiderman!"),
        Comment(text="I love Mary Jane!"),
    ]
)

user2 = User(
    username="tony",
    email_address="tonystark@test.com",
    comments=[
        Comment(text="I love ironman!"),
        Comment(text="I love pepper potts!"),
    ]
)

user3 = User(
    username="bruce",
    email_address="brucebanner@test.com",
    comments=[
        Comment(text="I love hulk!"),
        Comment(text="I love betty ross!"),
    ]
)

session.add_all([user1, user2, user3])
session.commit()