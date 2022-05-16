import os
from sqlalchemy import create_engine, exc


class Config:
    '''
    General configuration parent class
    
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    RANDOM_QUOTE_URL = "http://quotes.stormconsultancy.co.uk/{}.json"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://paulineapondi:1989@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
    '''
    
    
    
    
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,

}