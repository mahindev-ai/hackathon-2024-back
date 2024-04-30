from app.extensions import db

def get_all_sales():
    sales = db.child("sales").get()
    if sales and sales.val():
        filtered_users = [sale for sale in sale.val() if sale and sale.get("id") is not None]
        return filtered_sales if filtered_sales else []
    else:
        return []

def get_sale(sale_id):
    # Ejemplo: Obtener un usuario de la base de datos
    sale = db.child("sales").child(sales_id).get()
    return sale.val()

def create_sale(sale_data):
    new_sale = {
        "id": sale_data["id"],
        "seller": sale_data["seller"],
        "buyer": sale_data["buyer"],
        "material": sale_data["material"],
        "amount": sale_data["amount"],
        "price": sale_data["price"],
    }

    db.reference("sales").child(new_sale["id"]).set(new_sale)
    return new_sale

def update_sale(sale_id, updated_data):
    # Ejemplo: Actualizar un usuario en la base de datos
    user = get_sale(sale_id)
    if user:
        user.update(updated_data)
        db.child("sales").child(sale_id).update(sale)
        return user

def delete_sale(user_id):
    # Ejemplo: Eliminar un usuario de la base de datos
    db.child("sales").child(sale_id).remove()