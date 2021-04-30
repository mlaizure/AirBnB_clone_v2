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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display HTML page with state data from storage engine"""
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
