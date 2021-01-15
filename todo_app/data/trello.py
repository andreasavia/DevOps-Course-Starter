import requests
import json
import os


class TrelloDetails:

    def __init__(self):
        self.api_key = os.environ.get('TRELLO_API_KEY')
        self.api_token = os.environ.get('TRELLO_API_TOKEN')

        boards_response = requests.get("https://api.trello.com/1/members/me/boards/",
                                       params={'key': self.api_key, 'token': self.api_token})
        boards = json.loads(boards_response.text)

        for board in boards:
            board_name = board['name']
            board_closed = board['closed']

            if board_name == "To-Do App" and board_closed is False:
                self.id_board = board['id']
                break

        lists_response = requests.get("https://api.trello.com/1/boards/" + self.id_board + "/lists",
                                      params={'key': self.api_key, 'token': self.api_token})
        lists = json.loads(lists_response.text)
        for list in lists:
            if list['name'] == 'To-Do' and list['closed'] is False:
                self.id_list_todo = list['id']
            elif list['name'] == 'Doing' and list['closed'] is False:
                self.id_list_doing = list['id']
            elif list['name'] == 'Done' and list['closed'] is False:
                self.id_list_done = list['id']
