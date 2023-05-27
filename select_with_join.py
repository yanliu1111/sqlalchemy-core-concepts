from main import session
from models import User, Comment
from sqlalchemy import select

statement = select(Comment).join(Comment.user).where(User.username == 'bruce').order_by(Comment.id)

comments = session.scalars(statement).all()

for comment in comments:
    print(comment)

