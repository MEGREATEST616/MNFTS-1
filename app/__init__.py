import re
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from config import config
from flask_login import LoginManager
from celery import Celery
from flask_bootstrap import Bootstrap
import logging

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
celery = Celery()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    celery.conf.update(app.config)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    login_manager.init_app(app)
    logger = logging.getLogger('werkzeug')
    handler = TimedRotatingFileHandler(filename='web.log', when='midnight',
                                       backupCount=7, encoding='utf-8')
    handler.suffix = '%Y-%m-%d.log'
    handler.extMatch = re.compile(r'^\d{4}-\d{2}-\d{2}.og')
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    logger.addHandler(handler)
    return app


