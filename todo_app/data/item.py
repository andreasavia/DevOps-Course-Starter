from todo_app.data.trello import TrelloDetails
import requests
import json

URL = "https://api.trello.com/1/cards/"
trello = TrelloDetails()


class Item:

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def add(name):
        requests.post(URL,
                      params={'key': trello.api_key, 'token': trello.api_token, 'idList': trello.id_list_todo,
                              'name': name})

    def start(id):
        requests.put(URL + id,
                     params={'key': trello.api_key, 'token': trello.api_token, 'idList': trello.id_list_doing})

    def complete(id):
        requests.put(URL + id,
                     params={'key': trello.api_key, 'token': trello.api_token, 'idList': trello.id_list_done})

    def stop(id):
        requests.put(URL + id,
                     params={'key': trello.api_key, 'token': trello.api_token, 'idList': trello.id_list_todo})

    def reopen(id):
        requests.put(URL + id,
                     params={'key': trello.api_key, 'token': trello.api_token, 'idList': trello.id_list_todo})

    def archive(id):
        requests.put(URL + id,
                     params={'key': trello.api_key, 'token': trello.api_token, 'closed': 1})


def get_cards_in_list(id_list):
    response = requests.get("https://api.trello.com/1/lists/" + id_list + "/cards",
                            params={'key': trello.api_key, 'token': trello.api_token})
    return json.loads(response.text)


def get_items():

    items = []

    todo_items = get_cards_in_list(trello.id_list_todo)
    for todo_item in todo_items:
        item = Item(todo_item['id'], todo_item['name'], '0_todo')
        items.append(item)

    doing_items = get_cards_in_list(trello.id_list_doing)
    for doing_item in doing_items:
        item = Item(doing_item['id'], doing_item['name'], '1_doing')
        items.append(item)

    done_items = get_cards_in_list(trello.id_list_done)
    for done_item in done_items:
        item = Item(done_item['id'], done_item['name'], '2_done')
        items.append(item)

    return items
