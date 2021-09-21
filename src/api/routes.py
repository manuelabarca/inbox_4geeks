"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Product, Inbox
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200

@api.route('/messages/<int:id>', methods=["GET"])
def getMessages(id):
    messages = Inbox.getInbox(id)

    return jsonify({messages: messages}), 200


@api.route('/product', methods=["POST"])
def create_product():
    body = request.get_json()
    if body is None:
        return jsonify({"msg": "error body is null or empty"})
    
    name = body["name"]
    price = body["price"]
    user_id = body["user_id"]

    product = Product.create_product(name, price, user_id)

    return jsonify({"msg": "product created"}), 200