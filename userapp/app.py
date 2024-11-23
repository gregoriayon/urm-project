from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from userapp.routes import users

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:201830011@localhost/urm_db'

    db.init_app(app)

    # reegister all blueprints
    app.register_blueprint(users, url_prefix='/')

    migrate = Migrate(app, db)
    return app