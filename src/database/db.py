from pymongo import MongoClient

from src import env
from src.database.podatki.blog import blog
from src.database.podatki.global_error import global_error
from src.database.podatki.jaz import jaz
from src.database.podatki.hipnoterapija import hipnoterapija
from src.database.podatki.index import index
from src.database.podatki.jasnovidnost import jasnovidnost
from src.database.podatki.knjiga import knjiga
from src.database.podatki.medijstvo import medijstvo
from src.database.podatki.regresija import regresija
from src.database.podatki.samohipnoza import samohipnoza
from src.database.podatki.mediji import mediji

client = MongoClient(env.DB_CONNECTION)
proces = client[env.DB_PROCES]


def drop():
    proces.blog.drop()
    # proces.error.drop()
    # proces.mediji.drop()
    # proces.jaz.drop()
    # proces.hipnoterapija.drop()
# proces.index.drop()
    # proces.jasnovidnost.drop()
    # proces.knjiga.drop()
    # proces.medijstvo.drop()
    # proces.regresija.drop()
    # proces.samohipnoza.drop()


def seed():
    proces.blog.insert_many(blog)
    # proces.error.insert_many(global_error)
    # proces.mediji.insert_many(mediji)
    # proces.jaz.insert_many(jaz)
    # proces.hipnoterapija.insert_many(hipnoterapija)
# proces.index.insert_many(index)
    # proces.jasnovidnost.insert_many(jasnovidnost)
    # proces.knjiga.insert_many(knjiga)
    # proces.medijstvo.insert_many(medijstvo)
    # proces.regresija.insert_many(regresija)
    # proces.samohipnoza.insert_many(samohipnoza)
