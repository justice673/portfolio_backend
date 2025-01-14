from flask import Blueprint
from app.controllers.contact_controller import save_contact

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/submit', methods=['POST'])

def save_contact_route():
    return save_contact()
