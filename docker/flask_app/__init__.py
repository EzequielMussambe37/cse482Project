# Auhor: Jake Yax

from flask import Flask
from flask_failsafe import failsafe

@failsafe
def create_app():
    app = Flask(__name__)

    from .utils.database.database import database
    db = database()
    db.createTables(purge=True)

    with app.app_context():
        return app