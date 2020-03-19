from os import getenv

AMQP_URI = getenv('AMQP_URI')
# Default services exchange
AMQP_EXCHANGE = 'some-exchange'