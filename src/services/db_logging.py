from pymongo import MongoClient

from src import env

from src.database.logging import logging

client = MongoClient(env.DB_CONNECTION_LOGGING)
proces_log = client[env.DB_PROCES_LOGGING]


def drop_log():
    proces_log.logging.drop()
    pass


def seed_log():
    proces_log.logging.insert_many(logging)
    pass

