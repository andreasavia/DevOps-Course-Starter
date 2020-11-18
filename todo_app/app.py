from todo_app.data.session_items import get_items
from flask import Flask, render_template

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    # Modify the index() function to get the list of items and
    # update the index.html template to display their titles as a list.
    items = get_items()
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run()
