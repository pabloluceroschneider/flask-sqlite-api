import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class StageConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("STAGE_DATABASE_URL")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

config = {
    "development": DevelopmentConfig,
    "test": TestConfig,
    "stage": StageConfig,
    "prod": ProductionConfig
}
