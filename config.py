class Config:
    DB_NAME = "url-shortner"
    COLLECTION_NAME = "shortened_urls"


class DevelopmentConfig(Config):
    MONGO_DATABASE_URI = "mongodb://localhost:27017/"


class ProductionConfig(Config):
    pass
