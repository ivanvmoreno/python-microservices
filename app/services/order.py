import os
import connexion

from connexion.resolver import RestyResolver

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='openapi/')
    app.add_api('order.yaml', resolver=RestyResolver('api'))
    app.run(port=services.ORDER.PORT)
