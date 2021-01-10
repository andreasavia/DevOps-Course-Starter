from todo_app.flask_config import TRELLO_API_KEY, TRELLO_API_TOKEN

import requests
import json

query = {
   'key': TRELLO_API_KEY,
   'token': TRELLO_API_TOKEN
}

boards_response = requests.request(
   "GET",
   "https://api.trello.com/1/members/me/boards/",
   params=query
)

boards = json.loads(boards_response.text)

BOARD_ID = None
for board in boards:
   board_name = board['name']
   board_closed = board['closed']
   print("Evaluating Trello board " + board_name)
   
   if board_name == "To-Do App" and board_closed is False:
      BOARD_ID = board['id']
      print("Trello board " + board_name + " found!")
      break

if BOARD_ID is None:
   print("Trello board not found among existing ones and creating a new one for the To-Do App!")

lists_response = requests.request(
   "GET",
   "https://api.trello.com/1/boards/" + BOARD_ID + "/lists",
   params=query
)
lists = json.loads(lists_response.text)

todoList, doingList, doneList = False, False, False
for list in lists:
   if list['name'] == 'To-Do' and list['closed'] is False:
      todoList = True
   elif list['name'] == 'Doing' and list['closed'] is False:
      doingList = True
   elif list['name'] == 'Done' and list['closed'] is False:
      doneList = True

if todoList is True and doingList  is True and doneList is True:
   print("All required lists are present in the Trello board " + board_name)
else:
   print("The required lists for the To-Do App are present in " + board_name + 
   "\nPlease ensure the following lists are created: To-Do, Doing and Done")