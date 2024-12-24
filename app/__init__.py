from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
     
    from app.routes.contact_route import contact_bp
    from app.routes.realisations_route import realisation_bp
    
    app.register_blueprint(contact_bp, url_prefix='/api/contact')
    app.register_blueprint(realisation_bp, url_prefix='/api/realisations')
    
    return app
