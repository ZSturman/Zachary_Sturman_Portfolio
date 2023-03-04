import random
from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ZSDynamics"
    SECRET_KEY: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str

    class Config:
        env_file = "app/.env"

@lru_cache()
def get_settings():
    return Settings()

class Config(object):
    DEBUG = False
    TESTING = False

    DEV_TEST = False
    DEV_STATUS = False

    WELCOME_BASKET_LINK = 'https://www.youtube.com/watch?v=0qpuGNAek0c&list=PLTnRtjQN5iearIo2_C-2sr1ZqUHbS3Snh&index=8'

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = True
    MAIL_DEFAULT_SENDER = ("Zachary from ZSDynamics.com", "ZS@ZSDynamics.com")
    MAIL_MAX_EMAILS = 10

    APP_CONTEXT_PROCESSORS = ['app.context_processors.portfolio_context_processor']

class DevelopmentConfig(Config):
    DEBUG = True
    DEV_STATUS = True
    PERMANENT_SESSION_LIFETIME = 20
    
class ProductionConfig(Config):
    pass
class TestingConfig(Config):
    DEV_TEST = True
    PERMANENT_SESSION_LIFETIME = 20
    TESTING = True
