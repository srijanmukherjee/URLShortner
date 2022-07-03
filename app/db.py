from flask import current_app, g
import pymongo


def get_db_client():
    if "db" not in g:
        g.client = pymongo.MongoClient(current_app.config["MONGO_DATABASE_URI"])

    return g.client


def close_db_client(e=None):
    client: pymongo.MongoClient = g.pop("db", None)

    if client is not None:
        client.close()
