from main import session
from models import User

peter = session.query(User).filter_by( username ='bruce').first()
print(peter)