from todo_app.data.trello import TODO_LIST_ID, DOING_LIST_ID, DONE_LIST_ID
from todo_app.flask_config import TRELLO_API_KEY, TRELLO_API_TOKEN
import requests
import json

URL = "https://api.trello.com/1/cards/"


class Item:

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def add(name):
        requests.post(URL,
                      params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                              'idList': TODO_LIST_ID,
                              'name': name
                              }
                      )

    def start(id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': DOING_LIST_ID
                             }
                     )

    def complete(id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': DONE_LIST_ID
                             }
                     )

    def stop(id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': TODO_LIST_ID
                             }
                     )

    def reopen(id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': TODO_LIST_ID
                             }
                     )

    def archive(id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'closed': 1
                             }
                     )
