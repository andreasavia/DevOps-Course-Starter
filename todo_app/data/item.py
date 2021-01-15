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

    # def get_item():

    def add(name):
        requests.post(URL,
                      params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                              'idList': TODO_LIST_ID,
                              'name': name
                              }
                      )

    def start(self, id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': DOING_LIST_ID
                             }
                     )
        self.status = "doing"

    def complete(self, id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': DONE_LIST_ID
                             }
                     )
        self.status = "done"

    def stop(self, id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': TODO_LIST_ID
                             }
                     )
        self.status = "todo"

    def reopen(self, id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'idList': TODO_LIST_ID
                             }
                     )
        self.status = "todo"

    def archive(self, id):
        requests.put(URL + id,
                     params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN,
                             'closed': 1
                             }
                     )
        self.status = "closed"
