import logging
import sys
import os
from logging import FileHandler, StreamHandler


class Config:

    SAMPLE_SERVICE = os.getenv('SERVICE_NAME') or 'not set'
    ENV_CONFIG = os.getenv('ENV_CONFIG') or 'not set'
    CURRENT_VERSION = os.getenv('CURRENT_VERSION') or 'not set'
    DB_USER = os.getenv('DB_USER') or 'not set'
    DB_PASSWORD = os.getenv('DB_PASSWORD') or 'not set'
    DB_HOST = os.getenv('DB_HOST') or 'not set'
    DB_PORT = os.getenv('DB_PORT') or 'not set'
    DB_NAME = os.getenv('DB_NAME') or 'not set'

    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER,
                                                                   DB_PASSWORD,
                                                                   DB_HOST,
                                                                   DB_PORT,
                                                                   DB_NAME)

    @staticmethod
    def init_app(app, config_name, log_level=logging.INFO):
        log_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

        root_logger = logging.getLogger()

        # file_handler = FileHandler(config_name + '-application.log')
        # file_handler.setLevel(logging.INFO)
        # file_handler.setFormatter(log_formatter)
        # root_logger.addHandler(file_handler)

        console_handler = StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)


# inherits from Config baseclass
class UnitTestConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False

    @staticmethod
    def init_app(app, config_name, log_level=logging.DEBUG):
        super(UnitTestConfig, UnitTestConfig).init_app(app, config_name, log_level)


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app, config_name, log_level=logging.DEBUG):
        super(DevelopmentConfig, DevelopmentConfig).init_app(app, config_name, log_level)

    DEBUG = True


class UatConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = False

    @staticmethod
    def init_app(app, config_name, log_level=logging.DEBUG):
        super(UatConfig, UatConfig).init_app(app, config_name, log_level)


class ProdConfig(Config):
    DEBUG = True

    @staticmethod
    def init_app(app, config_name, log_level=logging.INFO):
        super(ProdConfig, ProdConfig).init_app(app, config_name, log_level)


config = {
    'DEV': DevelopmentConfig,
    'UAT': UatConfig,
    'PROD': ProdConfig,

    'default': DevelopmentConfig,
    'testing': UnitTestConfig
}
