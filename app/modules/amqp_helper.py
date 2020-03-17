import aiormq
import asyncio
from typing import *


class AMQPHelper:
    _connections: Dict[str, Dict]= {}
    # _exchanges holds the reference of a exchange to its parent channel
    _exchanges: Dict[str, Callable] = {}

    async def connect(self, amqp_uri, events_bindings: Dict[str, Callable], exchange_name=''):
        try:
            if exchange_name not in self._exchanges:
                if amqp_uri not in self._connections:
                    self._connections[amqp_uri] = { '_conn': await aiormq.connect(amqp_uri) }
                    self._connections[amqp_uri]['_ch'] = await self._connections[amqp_uri]['_conn'].channel()
                channel = self._connections[amqp_uri]['_ch']
                # Declare direct exchange
                await channel.exchange_declare(exchange=exchange_name, durable=True)
                for event_name, callback in events_bindings.items():
                    declared_queue = await channel.queue_declare(durable=True)
                    await channel.queue_bind(declared_queue.queue, exchange_name, routing_key=event_name)
                    # Start consumption of queue messages
                    await channel.basic_consume(declared_queue.queue, callback)
                self._exchanges[exchange_name] = channel
            else:
                raise ValueError('Already connected to server / exchange combination')
        except:
            print('Unexpected error when trying to connect')

    async def publish(self, exchange_name, event_name, body):
        if self._exchanges[exchange_name]:
            await self._exchanges[exchange_name].basic_publish(body, exchange=exchange_name, routing_key=event_name)
        else:
            raise ValueError('Channel not open for specified exchange. Check if existing connection to its server')

    def publish_sync(self, exchange_name, event_name, body):
        asyncio.run(self.publish(exchange_name, event_name, body))
