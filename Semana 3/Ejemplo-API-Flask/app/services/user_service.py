from app.repositories.user_repository import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

def create_user_service(data):
    if not data.get("name") or not data.get("email"):
        raise ValueError("name y email son obligatorios")

    return create_user(data["name"], data["email"])

def get_users_service():
    users = get_all_users()
    return [vars(u) for u in users]

def get_user_service(user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("Usuario no encontrado")
    return vars(user)

def update_user_service(user_id, data):
    if not data.get("name") or not data.get("email"):
        raise ValueError("Datos inválidos")

    if not get_user_by_id(user_id):
        raise ValueError("Usuario no existe")

    update_user(user_id, data["name"], data["email"])

def delete_user_service(user_id):
    if not get_user_by_id(user_id):
        raise ValueError("Usuario no existe")

    delete_user(user_id)
