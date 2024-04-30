from app.extensions import db

def get_all_users():
    users = db.reference("users").get()
    if len(users) == 0:
        return []
    else:
        return list(users.values())

def get_user(user_id):
    # Ejemplo: Obtener un usuario de la base de datos
    user = db.reference("users").child(user_id).get()
    return user.val()

def create_user(user_data):
    new_user = {
        "id": user_data["id"],
        "name": user_data["name"],
        "email": user_data["email"],
        "password": user_data["password"],
        "address": user_data["address"],
        "role": user_data.get("role", 1),  # Asignar un rol predeterminado si no se proporciona
    }
    if new_user["role"] == 0:
        new_user["role_name"] = "Administrador"
    elif new_user["role"] == 1:
        new_user["role_name"] = "Vendedor"
    else:
        new_user["role_name"] = "Reciclador"

    db.reference("users").child(new_user["id"]).set(new_user)
    return new_user

def update_user(user_id, updated_data):
    # Ejemplo: Actualizar un usuario en la base de datos
    user = get_user(user_id)
    if user:
        user.update(updated_data)
        db.reference("users").child(user_id).update(user)
        return user

def delete_user(user_id):
    # Ejemplo: Eliminar un usuario de la base de datos
    db.reference("users").child(user_id).remove()