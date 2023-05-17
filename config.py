import os
from datetime import timedelta


class Config:
    STATIC_FOLDER = "views/static/"
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + \
                              os.environ['PGSQL_USER'] + ':' + \
                              os.environ['PGSQL_PASSWORD'] + '@' + \
                              os.environ['PGSQL_HOST'] + ':' + \
                              os.environ['PGSQL_PORT'] + '/' + \
                              os.environ['PGSQL_DATABASE']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    ACCESS_EXPIRES = timedelta(hours=4)
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
    JWT_SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False


class Regexp:
    PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
    EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
