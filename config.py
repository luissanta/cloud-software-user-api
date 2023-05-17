from datetime import timedelta
from decouple import config


class Config:
    STATIC_FOLDER = "views/static/"
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + \
                              config('PGSQL_USER') + ':' + \
                              config('PGSQL_PASSWORD') + '@' + \
                              config('PGSQL_HOST') + ':' + \
                              config('PGSQL_PORT') + '/' + \
                              config('PGSQL_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    ACCESS_EXPIRES = timedelta(hours=4)
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
    JWT_SECRET_KEY = config('SECRET_KEY')
    DEBUG = False


class Regexp:
    PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
    EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
