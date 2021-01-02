from operator import itemgetter
from flask import session

_DEFAULT_ITEMS = [
    {'id': 1, 'status': 'Not Started', 'title': 'List saved todo items'},
    {'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added'}
]


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """

    return session.get('items', _DEFAULT_ITEMS)


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = {'id': id, 'title': title, 'status': 'Not Started'}

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id']
                     else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def complete_item(id):
    """
    Updates the status of an the item beloging at the given ID to 'Completed' and saves it

    Args:
        item: The item to complete
    """
    item = get_item(id)  # get item
    item['status'] = 'Completed'  # update status
    save_item(item)  # save item

    return item


def delete_item(id):
    """
    Deletes the item beloging at the given ID

    Args:
        item: The item to delete
    """

    items = get_items()  # get all items
    item = get_item(id)  # get all items

    idx = 0
    for item in items:
        if item['id'] == int(id):
            break
        idx = idx + 1

    items.pop(idx)  # remove given item
    session['items'] = items  # update items in session"""


def sort_items(order):
    """
    Updated the session based on the user's sort preference
    """
    items = get_items()
    if order == "0":
        updatedItems = sorted(items, key=itemgetter('id'))
        print("items order updated : 0")
    elif order == "1":
        updatedItems = sorted(items, key=itemgetter('status'))
        print("items order updated : 1")
    elif order == "2":
        updatedItems = sorted(items, key=itemgetter('status'), reverse=True)
        print("items order updated : 2")
    else:
        updatedItems = items
        print("items order NOT updated")

    session['items'] = updatedItems
