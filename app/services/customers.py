from ..modules.service_helper import ServiceHelper
from ..config.messaging import AMQP_CUSTOMERS
from ..config.constants import CONTROLLER_CUSTOMERS, DB_URI, OPENAPI_CUSTOMERS, TCP_PORT_CUSTOMERS

if __name__ == '__main__':
    service = ServiceHelper(OPENAPI_CUSTOMERS, CONTROLLER_CUSTOMERS, DB_URI, AMQP_CUSTOMERS, TCP_PORT_CUSTOMERS)
    service.run()