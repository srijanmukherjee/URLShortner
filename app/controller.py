import hashlib
from typing import Optional

from app.decorators import with_collection


cache = {}

# TODO: implement a cache decorator


@with_collection
def get_url(collection, urlid: str) -> Optional[dict]:
    if urlid in cache:
        return {"url": cache[urlid]}

    url = collection.find_one({"urlid": urlid})
    if url:
        cache[urlid] = url["url"]
    return url


@with_collection
def get_url_by_longurl(collection, longurl: str) -> Optional[dict]:
    url = collection.find_one({"url": longurl})
    return url


@with_collection
def create_tiny_url(collection, longurl: str) -> Optional[dict]:
    urlid = generate_tiny_key(longurl)

    collection.insert_one({"url": longurl, "urlid": urlid})

    return urlid


# TODO: improve the uniqueness of the key
def generate_tiny_key(longurl: str) -> str:
    return hashlib.md5(longurl.encode("utf-8")).hexdigest()[:7]
