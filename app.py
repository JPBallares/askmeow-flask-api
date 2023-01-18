import os
from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    from api.route.questions import questions_api

    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Ask Meow API',
    }
    swagger = Swagger(app)
    # Initialize Config
    app.config.from_pyfile('config.py')
    app.register_blueprint(questions_api, url_prefix='/api')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_USER'),
        os.getenv('DB_PASS'),
        os.getenv('DB_HOST'),
        os.getenv('DB_PORT'),
        os.getenv('DB_NAME'),
    )

    db.init_app(app)
    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
