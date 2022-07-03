import hashlib
from typing import Optional
from flask import current_app
import pymongo

from . import db


# TODO: add funciton decorater to get client
def get_url(urlid: str) -> Optional[dict]:
    db_name = current_app.config["DB_NAME"]
    collection_name = current_app.config["COLLECTION_NAME"]

    client: pymongo.MongoClient = db.get_db_client()
    collection = client[db_name][collection_name]
    url = collection.find_one({"urlid": urlid})
    return url


def get_url_by_longurl(longurl: str) -> Optional[dict]:
    db_name = current_app.config["DB_NAME"]
    collection_name = current_app.config["COLLECTION_NAME"]

    client: pymongo.MongoClient = db.get_db_client()
    collection = client[db_name][collection_name]
    url = collection.find_one({"url": longurl})
    return url


# TODO: handle error
def create_tiny_url(longurl: str) -> Optional[dict]:
    db_name = current_app.config["DB_NAME"]
    collection_name = current_app.config["COLLECTION_NAME"]

    client: pymongo.MongoClient = db.get_db_client()
    collection = client[db_name][collection_name]

    urlid = generate_tiny_key(longurl)

    collection.insert_one({"url": longurl, "urlid": urlid})

    return urlid


# TODO: improve the uniqueness of the key
def generate_tiny_key(longurl: str) -> str:
    return hashlib.md5(longurl.encode("utf-8")).hexdigest()[:7]
