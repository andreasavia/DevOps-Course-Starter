from flask import session

_DEFAULT_SORT = "descending"


def get_sorting():
    return session.get('sorting', _DEFAULT_SORT)


def set_sorting(preference):
    session['sorting'] = preference
