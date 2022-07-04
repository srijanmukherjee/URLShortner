class Config:
    DB_NAME = "url-shortner"
    COLLECTION_NAME = "shortened_urls"
    HOST = "http://127.0.0.1:5000"


class DevelopmentConfig(Config):
    MONGO_DATABASE_URI = "mongodb://localhost:27017/"


class ProductionConfig(Config):
    pass
