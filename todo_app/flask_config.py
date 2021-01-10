import os

TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
TRELLO_API_TOKEN = os.environ.get('TRELLO_API_TOKEN')

class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")    