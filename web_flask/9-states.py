#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    """remove current SQLAlchemy session"""
    storage.close()


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id):
    """display HTML page with city and state data from storage engine"""
    all_states = storage.all(State)
    if id:
        states = all_states.get('State.{}'.format(id))
    else:
        states = all_states.values()
    return render_template('9-states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
