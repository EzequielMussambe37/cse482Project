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
    config.read(os.path.join(os.path.dirname(__file__), 'static', 'config.ini'))
    app.config['STEAM_API_KEY'] = config.get('api', 'steamapikey')
    app.config['DATABASE_NAME'] = config.get('database', 'databasename')
    app.config['DATABASE_ENDPOINT'] = config.get('database', 'databaseendpoint')
    app.config['DATABASE_USER'] = config.get('database', 'databaseuser')
    app.config['DATABASE_PASSWORD'] = config.get('database', 'databasepassword')


    from .utils.database.database import database
    db = database()
    db.createTables(purge=True)

    with app.app_context():
        return app