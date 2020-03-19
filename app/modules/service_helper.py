from ..modules.amqp_helper import AMQPHelper
import connexion
from threading import Thread, Lock
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from connexion.resolver import RestyResolver


class ServiceHelperMeta(type):
    _instance = None
    # Lock object for thread-safe implementation
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                # Call to type.__new__ and type.__init__
                cls._instance = super().__call__(*args, **kwargs)
            return cls._instance


class ServiceHelper(metaclass=ServiceHelperMeta):
    def __init__(self, openapi_path, controller_name, db_uri, amqp_config, server_port):
        """
        :param openapi_path: tuple (spec directory, specification filename)
        :param controller_name: service controller module name
        :param db_uri: MYSQL database connection URI
        :param amqp_config: service AMQP config dictionary
        :param server_port: TCP port for Flask to listen on
        """
        self._connexion = connexion.FlaskApp(__name__, specification_dir='../{}'.format(openapi_path[0]))
        self._connexion.add_api(openapi_path[1], resolver=RestyResolver(controller_name))
        self._app = self._connexion.app
        self._app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        self._app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # Service database connection instance
        self.db = SQLAlchemy(self._app)
        self._ma = Marshmallow(self._app)
        self._amqp_config = amqp_config
        self._server_port = server_port

    def amqp_connect(self):
        amqp = AMQPHelper()
        for amqp_uri, uri_config in self._amqp_config.items():
            for exchange_name, events_bindings in uri_config.items():
                amqp.connect(amqp_uri, events_bindings, exchange_name)
            # Start consuming connection queues
            Thread(target=amqp.start_consuming, args=[amqp_uri]).start()

    def run_webserver(self):
        Thread(target=self._app.run, kwargs={'port': self._server_port}).start()

    def run(self):
        self.run_webserver()
        self.amqp_connect()
