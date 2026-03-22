from flask import Blueprint, request, jsonify
from app.services.user_service import *

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('', methods=['POST'])
def create():
    try:
        user_id = create_user_service(request.get_json())
        return jsonify({"id": user_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route('', methods=['GET'])
def get_all():
    return jsonify(get_users_service())


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_one(user_id):
    try:
        return jsonify(get_user_service(user_id))
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    try:
        update_user_service(user_id, request.get_json())
        return jsonify({"message": "Usuario actualizado"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    try:
        delete_user_service(user_id)
        return jsonify({"message": "Usuario eliminado"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404