from os import getenv

# TCP ports services listen to 
TCP_PORT_CUSTOMERS = 8001
TCP_PORT_NOTIFICATIONS = 8002
TCP_PORT_ORDERS = 8003
TCP_PORT_PRODUCTS = 8004

# OpenAPI specifications project directory (relative to app/)
OPENAPI_DIR = 'openapi/'
OPENAPI_CUSTOMERS = 'customers.yaml'
OPENAPI_ORDERS = 'orders.yaml'
OPENAPI_PRODUCTS = 'products.yaml'

# Module containing implementations of OpenAPI operationIDs
CONTROLLER_CUSTOMERS = 'app.controllers.customers_controller'
CONTROLLER_ORDERS = 'app.controllers.orders_controller'
CONTROLLER_PRODUCTS = 'app.controllers.products_controller'

DB_URI = getenv('DB_URI')
AMQP_URI = getenv('AMQP_URI')
