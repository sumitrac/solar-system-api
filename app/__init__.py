from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
   
    
    if not test_config:
        app.config['TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_solar_system_development'] = os.environ.get(
            "SQLALCHEMY_DATABASE_solar_system_development")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_solar_system_development"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_solar_system_test")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.planet import Planet
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app

