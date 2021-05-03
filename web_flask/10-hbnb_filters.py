#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    """remove current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display HTML page with dropdowns"""
    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=all_states,
                           amenities=all_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
