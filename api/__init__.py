from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api

from .auth.view import auth_namespace
from .config.config import config_dict
from .models.orders import Order
from .models.users import User
from .orders.view import order_namespace
from .utils.db import db
from werkzeug.exceptions import NotFound, MethodNotAllowed


def create_app(config=config_dict['dev']):
    app=Flask(__name__)
    
    app.config.from_object(config)

    authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            'description': "Add a JWT with ** Bearer &lt;JWT&gt; to authorize"
        }
    }

    api=Api(app,
        title='Order and Delivery Management System',
        description='This is a simple order and delivery management system',
        authorizations=authorizations,
        security='Bearer Auth',
        )

    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace, path='/auth')

    db.init_app(app)

    jwt=JWTManager(app)

    migrate = Migrate(app, db)

    #error handler for 404
    @api.errorhandler(NotFound)
    def not_found(error):
        return {'error': 'Not found'}, 404
    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {'error': 'Method not allowed'}, 405


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User,
            'Order':Order,
        }

    return app