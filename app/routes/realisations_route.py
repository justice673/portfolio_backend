from flask import Blueprint
from app.controllers.realisations_controller import get_realisations

realisation_bp = Blueprint('realisation', __name__)
 
@realisation_bp.route('/create', methods=['GET'])

def get_realisations_route():
    return get_realisations()