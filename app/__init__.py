from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
<<<<<<< HEAD
    
    from app.models.planet import Planet

    
=======

    
    from app.models.planet import Planet


>>>>>>> e92ddc2aaa6ebaa6fa27d992c591c4a871a326c1
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import planets_bp
    app.register_blueprint(planets_bp)


    return app

