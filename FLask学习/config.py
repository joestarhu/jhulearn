import os,random

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(random.random())
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB_URL') or 'sqlite:////' + os.path.join(basedir,'devapp.db')

class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') or 'sqlite:////' + os.path.join(basedir,'app.db')
