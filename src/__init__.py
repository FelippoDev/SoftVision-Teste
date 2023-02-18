from flask import Flask
from src.api.urls import api
from src.db import db, ma
from src import models


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(api)
    
    return app





