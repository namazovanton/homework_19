from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    configure_app(application)
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
