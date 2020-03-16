import aiormq, typing

class AMQPConnection:
    _connected = False

    def __init__(self, amqp_uri, events_bindings: typing.Dict[str, typing.Callable], exchage_name = ''):
        self.amqp_uri = amqp_uri
        self.events_bindings = events_bindings
        self.exchange_name = exchage_name

    async def connect(self):
        if not self._connected:
            self._connection = await aiormq.connect(self.amqp_uri)
            self._channel = await self._connection.channel()
            # Declare a direct exchange
            await self._channel.exchange_declare(exchange=self.exchange_name, durable=True)
            for event_name, callback in self.events_bindings.items():
                declared_queue = await self._channel.queue_declare(durable=True)
                await self._channel.queue_bind(declared_queue.queue, self.exchange_name, routing_key=event_name)
                # Start consumption of queue messages
                await self._channel.basic_consume(declared_queue.queue, callback)
            self._connected = True
        else:
            raise ValueError('Instance already connected to server')

    async def publish(self, event_name, body):
        if self._connected:
            await self._channel.basic_publish(body, exchange=self.exchange_name, routing_key=event_name)
        else:
            raise ValueError('Channel not open. Check instance connection')

