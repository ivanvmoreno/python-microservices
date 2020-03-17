from ..modules.amqp_helper import AMQPHelper
import asyncio
import connexion
from threading import Thread
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from connexion.resolver import RestyResolver


class ServiceHelper:
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
        self._db = SQLAlchemy(self._app)
        self._ma = Marshmallow(self._app)
        self._amqp_config = amqp_config
        self._server_port = server_port

    def handle_amqp_connection(self):
        loop = asyncio.new_event_loop()
        for amqp_uri, uri_config in self._amqp_config.items():
            for exchange_name, events_bindings in uri_config.items():
                loop.run_until_complete(AMQPHelper().connect(amqp_uri, events_bindings, exchange_name))
        # Locks execution thread
        loop.run_forever()

    def run_webserver(self):
        # Locks execution thread
        self._app.run(port=self._server_port)

    def run(self):
        Thread(target=self.handle_amqp_connection).start()
        Thread(target=self.run_webserver).start()