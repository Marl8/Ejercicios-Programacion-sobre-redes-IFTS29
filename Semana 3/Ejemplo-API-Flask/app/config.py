import os

class Config:
    DATABASE = os.path.join(os.getcwd(), 'database.db')
    DEBUG = True