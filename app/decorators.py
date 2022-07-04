from flask import current_app
import pymongo

from . import db


def with_collection(func):
    def wrapper(*args, **kwargs):
        with current_app.app_context():
            db_name = current_app.config["DB_NAME"]
            collection_name = current_app.config["COLLECTION_NAME"]
            client: pymongo.MongoClient = db.get_db_client()
            collection = client[db_name][collection_name]

        return func(collection, *args, **kwargs)

    return wrapper
