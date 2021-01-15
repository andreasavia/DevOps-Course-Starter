from todo_app.data.item import Item, get_items
from todo_app.data.session import set_sorting
from flask.globals import request
from flask.helpers import url_for
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
    item_name = request.form.get('newItem')
    Item.add(item_name)
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    Item.complete(id)
    return redirect(url_for('index'))


@app.route('/delete/<id>')
def delete(id):
    Item.archive(id)
    return redirect(url_for('index'))


@app.route('/sort/<order>')
def sort(order):
    set_sorting(order)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
