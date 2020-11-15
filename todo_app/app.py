from flask import Flask, render_template, request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    # Modify the index() function to get the list of items and
    # update the index.html template to display their titles as a list.
    return render_template('layout.html')


if __name__ == '__main__':
    app.run()
