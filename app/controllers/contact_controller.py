from flask import request, jsonify
from app.models.contact import Contact
from app import db

def save_contact():
    data = request.json
    try:
        new_contact = Contact(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "Contact saved successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
