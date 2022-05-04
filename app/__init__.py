from flask import Flask
from flask_bootstrap import Bootstrap
from .main import main as main_blueprint
from .request import configure_request
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):
# this will initialize the application
    app = Flask(__name__)
# instance_relative_config = True)
# set up configurations
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')
    
    app.register_blueprint(main_blueprint)
    # from app import views
    bootstrap.init_app(app)

    # setting config
    
    configure_request(app)

    return app
