from pymongo import MongoClient

from src import env
from src.database.blog import blog
from src.database.mediji import mediji
from src.database.user import user

client = MongoClient(env.DB_CONNECTION)
proces = client[env.DB_PROCES]


def drop():
    proces.user.drop()
    proces.blog.drop()
    proces.mediji.drop()
    pass


def seed():
    proces.user.insert_many(user)
    proces.blog.insert_many(blog)
    proces.mediji.insert_many(mediji)
    pass
