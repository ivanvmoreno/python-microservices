from os import getenv

# Default services exchange
AMQP_URI = getenv('AMQP_URI')
AMQP_EXCHANGE = 'some-exchange'