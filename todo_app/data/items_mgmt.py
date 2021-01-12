from todo_app.flask_config import TRELLO_API_KEY, TRELLO_API_TOKEN
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
        print("Evaluating Trello board " + board_name)

        if board_name == "To-Do App" and board_closed is False:
            board_id = board['id']
            print("Trello board " + board_name + " found!")
            break

    if board_id is None:
        print("Trello board not found among existing ones and creating a new one for the To-Do App!")

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


def get_items():
    board_id = get_board_id()
    idLists = get_lists_id(board_id)

    todo_items = get_cards_in_list(idLists['todo'])
    for todo_item in todo_items:
        todo_item['status'] = 'to_do'

    doing_items = get_cards_in_list(idLists['doing'])
    for doing_item in doing_items:
        doing_item['status'] = 'doing'

    done_items = get_cards_in_list(idLists['done'])
    for done_item in done_items:
        done_item['status'] = 'done'

    return todo_items + doing_items + done_items


def get_cards_in_list(id_list):
    response = requests.get(
        "https://api.trello.com/1/lists/" + id_list + "/cards",
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_API_TOKEN,
        }
    )
    return json.loads(response.text)


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


def sort_items():
    return get_items()
