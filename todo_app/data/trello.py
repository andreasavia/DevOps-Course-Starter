from todo_app.flask_config import TRELLO_API_KEY, TRELLO_API_TOKEN
import requests
import json


class TrelloDetails:

    ''' setup function to set 
    TODO_LIST_ID = lists_id['todo']
    DOING_LIST_ID = lists_id['doing']
    DONE_LIST_ID = lists_id['done']
    as well as Trelli Key and Token'''


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


BOARD_ID = get_board_id()
lists_id = get_lists_id(BOARD_ID)
TODO_LIST_ID = lists_id['todo']
DOING_LIST_ID = lists_id['doing']
DONE_LIST_ID = lists_id['done']
