from os import getenv

# Flask web server TCP port
TCP_PORT = 8001

# OpenAPI specifications directory (relative to 'app' module)
OPENAPI_PATH = ('openapi/', 'customers.yaml')

# Module containing implementations of OpenAPI operationIDs
CONTROLLER_MODULE = 'app.services.customers.controllers.customers_controller'

DB_URI = getenv('DB_URI')
