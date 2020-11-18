from flask.globals import request
from flask.helpers import url_for
from todo_app.data.session_items import add_item, get_items
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


if __name__ == '__main__':
    app.run(debug=True)
