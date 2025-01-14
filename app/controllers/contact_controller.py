from flask import request, jsonify
from app.models.contact import Contact
from app import db, mail
from flask_mail import Message
from werkzeug.exceptions import BadRequest

def save_contact():
    data = request.json
    # Basic validation
    if not all(field in data for field in ["first_name", "last_name", "email", "message"]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Save contact data to database
        new_contact = Contact(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            message=data["message"],
        )
        db.session.add(new_contact)
        db.session.commit()

        # Send email
        send_contact_email(data)

        return jsonify({"message": "Contact saved successfully!"}), 201

    except BadRequest as e:
        return jsonify({"error": f"Invalid data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def send_contact_email(data):
    # Send the email after saving to database
    msg = Message(
        "New Contact Form Submission",
        recipients=["bighush57@gmail.com"],  # Replace with your email
        body=f"Name: {data['first_name']} {data['last_name']}\n"
             f"Email: {data['email']}\n"
             f"Message:\n{data['message']}"
    )
    mail.send(msg)
