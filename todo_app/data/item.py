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


def get_cards_in_list(id_list):
    response = requests.get(
        "https://api.trello.com/1/lists/" + id_list + "/cards",
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_API_TOKEN,
        }
    )
    return json.loads(response.text)


def get_items():

    items = []

    todo_items = get_cards_in_list(TODO_LIST_ID)
    for todo_item in todo_items:
        item = Item(todo_item['id'], todo_item['name'], '0_to_do')
        items.append(item)

    doing_items = get_cards_in_list(DOING_LIST_ID)
    for doing_item in doing_items:
        item = Item(doing_item['id'], doing_item['name'], '1_doing')
        items.append(item)

    done_items = get_cards_in_list(DONE_LIST_ID)
    for done_item in done_items:
        item = Item(done_item['id'], done_item['name'], '2_done')
        items.append(item)

    return items
