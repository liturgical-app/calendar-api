import os


class Config(object):
    # General
    DEBUG = os.environ['DEBUG']
    PORT = os.environ['PORT']