from pymongo import MongoClient

from src import env
# from src.database.newsletter import newsletter
# from src.database.email import email
# from src.database.blog import blog
# from src.database.mediji import mediji
# from src.database.user import user
# from src.database.event import event
# from src.database.subscriber import subscriber

client = MongoClient(env.DB_CONNECTION)
proces = client[env.DB_PROCES]


def drop():
    # proces.user.drop()
    # proces.blog.drop()
    # proces.mediji.drop()
    # proces.email.drop()
    # proces.event.drop()
    # proces.subscriber.drop()
    # proces.newsletter.drop()
    pass


def seed():
    # proces.user.insert_many(user)
    # proces.blog.insert_many(blog)
    # proces.mediji.insert_many(mediji)
    # proces.email.insert_many(email)
    # proces.event.insert_many(event)
    # proces.subscriber.insert_many(subscriber)
    # proces.newsletter.insert_many(newsletter)
    pass
