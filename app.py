from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
from  flask_jwt_extended  import  JWTManager

from api.routes import create_routes


def get_flask_app(config: dict = None):
    flask_app = Flask(__name__)

    flask_app.config['MONGODB_HOST'] = 'YOUR_HOST'
    flask_app.config['JWT_SECRET_KEY'] = 'KEY'

    api = Api(app=flask_app)
    create_routes(api=api)

    db = MongoEngine(app=flask_app)

    jwt  =  JWTManager ( app = flask_app )

    return flask_app


if __name__ == '__main__':
    app = get_flask_app()   
    app.run(debug=True)
