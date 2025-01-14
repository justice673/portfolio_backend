from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
     
    from app.routes.contact_route import contact_bp
    
    app.register_blueprint(contact_bp, url_prefix='/api/contact')
    
    return app
