# Auhor: Jake Yax
import os
from flask import Flask
from flask_failsafe import failsafe
import configparser

@failsafe
def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(16)

    config = configparser.ConfigParser()
    config.read('static/config.ini')
    app.config['STEAM_API_KEY'] = config.get('api', 'steamapikey')
    app.config['']

    from .utils.database.database import database
    db = database()
    db.createTables(purge=True)

    with app.app_context():
        return app