from os import getenv

# TCP ports services listen to 
TCP_PORT_CUSTOMERS = 8001
TCP_PORT_NOTIFICATIONS = 8002
TCP_PORT_ORDERS = 8003
TCP_PORT_PRODUCTS = 8004

DB_URI = getenv('DB_URI')
AMQP_URI = getenv('AMQP_URI')
