import pika
from threading import Lock
from typing import *


class AMQPHelperMeta(type):
    _instance = None
    # Lock object for thread-safe implementation
    _lock: Lock = Lock()

    def __call__(cls):
        with cls._lock:
            if not cls._instance:
                # Call to type.__new__ and type.__init__
                cls._instance = super().__call__()
            return cls._instance


class AMQPHelper(metaclass=AMQPHelperMeta):
    _connections: Dict[str, Dict] = {}
    # _exchanges holds the reference of a exchange to its parent channel
    _exchanges: Dict[str, Callable] = {}

    def connect(self, amqp_uri, events_bindings: Dict[str, Callable], exchange_name):
        if exchange_name not in self._exchanges:
            if amqp_uri not in self._connections:
                self._connections[amqp_uri] = {'_conn': pika.BlockingConnection(pika.URLParameters(amqp_uri))}
                self._connections[amqp_uri]['_ch'] = self._connections[amqp_uri]['_conn'].channel()
            channel = self._connections[amqp_uri]['_ch']
            # Declare direct exchange
            channel.exchange_declare(exchange=exchange_name, durable=True)
            for event_name, callback in events_bindings.items():
                declared_queue = channel.queue_declare(queue=event_name)
                channel.queue_bind(event_name, exchange_name, routing_key=event_name)
                # Define queue callback function
                channel.basic_consume(event_name, callback, auto_ack=True)
            self._exchanges[exchange_name] = channel
        else:
            raise ValueError('Already connected to server / exchange combination')

    def publish(self, exchange_name, event_name, body):
        if self._exchanges[exchange_name]:
            self._exchanges[exchange_name].basic_publish(
                body=body, exchange=exchange_name, routing_key=event_name)
        else:
            raise ValueError('Channel not open for specified exchange. Check if existing connection to its server')

    def start_consuming(self, amqp_uri):
        # Start consumption of queues
        self._connections[amqp_uri]['_ch'].start_consuming()
