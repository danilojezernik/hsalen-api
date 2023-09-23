from pymongo import MongoClient

from src import env
from src.database.podatki.blog import blog
from src.database.podatki.global_error import global_error
from src.database.podatki.mediji import mediji

client = MongoClient(env.DB_CONNECTION)
proces = client[env.DB_PROCES]


def drop():
    proces.blog.drop()
    proces.error.drop()
    proces.mediji.drop()
    pass


def seed():
    proces.blog.insert_many(blog)
    proces.error.insert_many(global_error)
    proces.mediji.insert_many(mediji)
    pass
