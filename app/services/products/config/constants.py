from os import getenv

# Flask web server TCP port
TCP_PORT = 8003

# OpenAPI specifications directory (relative to 'app' module)
OPENAPI_PATH = ('openapi/', 'products.yaml')

# Module containing implementations of OpenAPI operationIDs
CONTROLLER_MODULE = 'app.services.products.controllers.products_controller'

DB_URI = getenv('DB_URI')
