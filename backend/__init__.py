from flask import Flask
from flask_cors import CORS


def create_app(debug=False):
    app = Flask(__name__)
    CORS(app)
    app.debug = debug

    from .database.database import Database
    db = Database()
    db.createTables(purge=True)

    with app.app_context():
        from . import routes
        return app