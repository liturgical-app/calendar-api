import os


class Config(object):
    # General
    DEBUG = os.getenv('DEBUG', 'True')
    PORT = os.getenv('PORT', '3000')