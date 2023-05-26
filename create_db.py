from connect import engine
from tables import users_table, comments_table, meta_obj

print('>>> Creating tables...')
meta_obj.create_all(bind=engine)