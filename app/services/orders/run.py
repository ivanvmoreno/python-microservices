from .config.messaging import AMQP_CONFIG
from .config.constants import CONTROLLER_MODULE, DB_URI, TCP_PORT, OPENAPI_PATH
from app.modules.service_helper import ServiceHelper

if __name__ == '__main__':
    service = ServiceHelper(OPENAPI_PATH, CONTROLLER_MODULE, DB_URI, AMQP_CONFIG, TCP_PORT)
    service.run()
