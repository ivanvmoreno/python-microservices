from os import getenv

# Flask web server TCP port
TCP_PORT = 8002

# OpenAPI specifications directory (relative to 'app' module)
OPENAPI_PATH = ('openapi/', 'orders.yaml')

# Module containing implementations of OpenAPI operationIDs
CONTROLLER_MODULE = 'app.services.orders.controllers.orders_controller'

DB_URI = getenv('DB_URI')
