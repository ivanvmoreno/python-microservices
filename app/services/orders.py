from .config import app
from connexion.resolver import RestyResolver

if __name__ == '__main__':
    app.add_api('order.yaml', resolver=RestyResolver('api'))
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.run(port=)
