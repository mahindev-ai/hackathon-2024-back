from app.extensions import db

def get_all_users():
    users = db.child("users").get()
    if users and users.val():
        filtered_users = [user for user in users.val() if user and user.get("id") is not None]
        return filtered_users if filtered_users else []
    else:
        return []



def get_user(user_id):
    # Ejemplo: Obtener un usuario de la base de datos
    user = db.child("users").child(user_id).get()
    return user.val()

def create_user(user_data):
    new_user = {
        "id": user_data["id"],
        "username": user_data["username"],
        "password": user_data["password"],
        "role": user_data.get("role", 1),  # Asignar un rol predeterminado si no se proporciona
    }
    if new_user["role"] == 0:
        new_user["role_name"] = "Administrador"
    elif new_user["role"] == 1:
        new_user["role_name"] = "Vendedor"
    else:
        new_user["role_name"] = "Reciclador"

    db.child("users").child(new_user["id"]).set(new_user)
    return new_user

def update_user(user_id, updated_data):
    # Ejemplo: Actualizar un usuario en la base de datos
    user = get_user(user_id)
    if user:
        user.update(updated_data)
        db.child("users").child(user_id).update(user)
        return user

def delete_user(user_id):
    # Ejemplo: Eliminar un usuario de la base de datos
    db.child("users").child(user_id).remove()