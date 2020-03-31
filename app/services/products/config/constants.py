from os import getenv

# OpenAPI specifications directory (relative to 'app' module)
OPENAPI_PATH = ('openapi/', 'products.yaml')

# Module containing implementations of OpenAPI operationIDs
CONTROLLER_MODULE = '.controllers.products_controller'

DB_URI = getenv('DB_URI')
