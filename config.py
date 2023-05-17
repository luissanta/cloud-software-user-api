import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()


class Config:
    STATIC_FOLDER = "views/static/"
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + \
                              os.environ.get('PGSQL_USER') + ':' + \
                              os.environ.get('PGSQL_PASSWORD') + '@' + \
                              os.environ.get('PGSQL_HOST') + ':' + \
                              os.environ.get('PGSQL_PORT') + '/' + \
                              os.environ.get('PGSQL_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    ACCESS_EXPIRES = timedelta(hours=4)
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False


class Regexp:
    PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
    EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
