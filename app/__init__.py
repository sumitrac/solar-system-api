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
=======
<<<<<<< HEAD
>>>>>>> dbb1515f123f3ae19e82a2a93370d5abb04d8b6e
    
    from app.models.planet import Planet

    
=======
    from app.models.planet import Planet

>>>>>>> 01b1c1f83f145fe269ccc58f1314086f928e1e35
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import planet_bp
    app.register_blueprint(planet_bp)


    return app

