from flask import Blueprint, request, jsonify
from models import add_message, get_pending_messages, get_messages_due_today
from utils import validate_date
from datetime import datetime

# Create a Blueprint for routes
routes = Blueprint("routes", __name__)

@routes.route("/schedule", methods=["POST"])
def schedule_message():
    data = request.get_json()
    if not data or "message" not in data or "delivery_date" not in data or "recipient" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    message = data["message"]
    delivery_date = data["delivery_date"]
    recipient = data["recipient"]

    # Validate the delivery date
    if not validate_date(delivery_date):
        return jsonify({"error": "Invalid date format or date not in future"}), 400

    add_message(message, delivery_date, recipient)
    return jsonify({"status": "Message scheduled successfully"}), 201

@routes.route("/pending", methods=["GET"])
def get_pending():
    messages = get_pending_messages()
    result = [
        {"id": msg[0], "message": msg[1], "delivery_date": msg[2], "recipient": msg[3], "created_at": msg[4]}
        for msg in messages
    ]
    return jsonify(result), 200

@routes.route("/deliver-today", methods=["GET"])
def deliver_today():
    messages = get_messages_due_today()
    result = [
        {"id": msg[0], "message": msg[1], "delivery_date": msg[2], "recipient": msg[3], "created_at": msg[4]}
        for msg in messages
    ]
    # Simulate delivery by printing to console (could be extended to email later)
    for msg in result:
        print(f"Delivering to {msg['recipient']}: {msg['message']}")
    return jsonify(result), 200