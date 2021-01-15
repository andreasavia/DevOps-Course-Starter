from operator import itemgetter
from todo_app.flask_config import TRELLO_API_KEY, TRELLO_API_TOKEN
from todo_app.data.item import Item
import requests
import json


def get_board_id():
    boards_response = requests.get(
        "https://api.trello.com/1/members/me/boards/",
        params={'key': TRELLO_API_KEY, 'token': TRELLO_API_TOKEN}
    )
    boards = json.loads(boards_response.text)
    board_id = None
    board_name = None

    for board in boards:
        board_name = board['name']
        board_closed = board['closed']

        if board_name == "To-Do App" and board_closed is False:
            board_id = board['id']
            break

    # if board_id is None:
    return board_id


def get_lists_id(board_id):
    lists_response = requests.get(
        "https://api.trello.com/1/boards/" + board_id + "/lists",
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_API_TOKEN
        }
    )

    lists = json.loads(lists_response.text)
    idLists = {'todo': '', 'doing': '', 'done': ''}
    for list in lists:
        if list['name'] == 'To-Do' and list['closed'] is False:
            idLists['todo'] = list['id']
        elif list['name'] == 'Doing' and list['closed'] is False:
            idLists['doing'] = list['id']
        elif list['name'] == 'Done' and list['closed'] is False:
            idLists['done'] = list['id']

    if idLists['todo'] != '' and idLists['doing'] != '' and idLists['done'] != '':
        print("All required lists are present in the board")
    else:
        print("The required lists for the To-Do App are present in the board" +
              "\nPlease ensure the following lists are created: To-Do, Doing and Done")
    return idLists


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
    board_id = get_board_id()
    idLists = get_lists_id(board_id)

    items = []

    todo_items = get_cards_in_list(idLists['todo'])
    for todo_item in todo_items:
        item = Item(todo_item['id'], todo_item['name'], '0_to_do')
        items.append(item)

    doing_items = get_cards_in_list(idLists['doing'])
    for doing_item in doing_items:
        item = Item(doing_item['id'], doing_item['name'], '1_doing')
        items.append(item)

    done_items = get_cards_in_list(idLists['done'])
    for done_item in done_items:
        item = Item(done_item['id'], done_item['name'], '2_done')
        items.append(item)

    return items


def add_item(title):
    board_id = get_board_id()
    idLists = get_lists_id(board_id)
    requests.post(
        "https://api.trello.com/1/cards/",
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_API_TOKEN,
            'idList': idLists['todo'],
            'name': title
        }
    )


def complete_item(id):
    board_id = get_board_id()
    idLists = get_lists_id(board_id)

    requests.put(
        "https://api.trello.com/1/cards/" + id,
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_API_TOKEN,
            'idList': idLists['done']
        }
    )


def delete_item(id):
    requests.put(
        "https://api.trello.com/1/cards/" + id,
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_API_TOKEN,
            'closed': 1
        }
    )


def sort_items(order):
    items = get_items()
    if order == "0":
        sorted_items = sorted(items, key=itemgetter('id'))
        print(sorted_items)
        print("items order updated : 0")
    elif order == "1":
        sorted_items = sorted(items, key=itemgetter('status'))
        print(sorted_items)
        print("items order updated : 1")
    elif order == "2":
        sorted_items = sorted(items, key=itemgetter('status'), reverse=True)
        print(sorted_items)
        print("items order updated : 2")
    else:
        sorted_items = items
        print("items order NOT updated")
    return sorted_items
