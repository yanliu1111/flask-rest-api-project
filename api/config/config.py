import os
import re
from datetime import timedelta
from decouple import config

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

uri = config("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# or set key directly:


class Config:
    SECRET_KEY=config('SECRET_KEY','secret')
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True
    DEBUG=True

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI="sqlite://" #database is going to be in memory is by simply giving sqlite this db
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=uri
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=config('DEBUG',cast=bool)

config_dict={
    'dev':DevConfig,
    'testing':TestConfig,
    'prodution':ProdConfig 
}