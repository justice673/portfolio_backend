from flask import jsonify
from app.models.realisation import Realisation

def get_realisations():
    realisations = Realisation.query.all()
    results = [
        {"id": r.id, "title": r.title, "description": r.description, "image": r.image, "price": r.price, "category": r.category}
        for r in realisations
    ]
    return jsonify(results), 200
