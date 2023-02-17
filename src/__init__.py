from flask import Flask
from src.api.urls import api
from src.db import db, ma
from src import models


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    # app.config['PROPAGATE_EXCEPTIONS'] = True
    # app.config['API_TITLE'] = "SOFT-VISION TEST"
    # app.config['API_VERSION'] = 'v1'
    # app.config['OPENAPI_VERSION'] = '3.0.3'
    # app.config['OPENAPI_URL_PREFIX'] = '/'
    # app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    # app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(api)
    
    return app





