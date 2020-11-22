from operator import itemgetter
from flask.globals import request
from flask.helpers import url_for
from todo_app.data.session_items import add_item, get_items, complete_item
from flask import Flask, render_template, redirect

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add():
    add_item(request.form.get('newItem'))
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    complete_item(id)
    return redirect(url_for('index'))


@app.route('/sort', methods=['POST'])
def sort():
    items = get_items()
    if request.form['sort_button'] == "Completed First":
        sorted_items = sorted(items, key=itemgetter('status'))
    if request.form['sort_button'] == "Not Started First":
        sorted_items = sorted(items, key=itemgetter('status'), reverse=True)
    if request.form['sort_button'] == "Default Order":
        return redirect(url_for('index'))
    return render_template('index.html', items=sorted_items)


if __name__ == '__main__':
    app.run(debug=True)
