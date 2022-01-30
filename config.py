import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = "moody200011123@gmail.com"
    MAIL_PASSWORD = 'xaxellaqkgtppelm'
    FLASKY_MAIL_SUBJECT_PREFIX = '[CP.]'
    FLASKY_MAIL_SENDER = 'moody200011123@gmail.com'
    FLASK_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    CELERY_BROKER_URL = 'amqp://root:root@127.0.0.1/dispatch_server_host'
    CELERY_RESULT_BACKEND = 'amqp://root:root@127.0.0.1/dispatch_server_host'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
    CELERY_ACCEPT_CONTENT = ["json"]

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev'
                                                                                                      '.sqlite')

    def init_app(app):
        Config.init_app(app)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqilite')


    # def init_app(app):
    #     Config.init_app(app)
    #     handler = logging.FileHandler('flask.log', encoding='UTF-8')
    #     logging_format = logging.Formatter(
    #         '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    #     handler.setFormatter(logging_format)
    #     app.logger.addHandler(handler)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
