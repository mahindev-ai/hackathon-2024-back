from app.extensions import db

def get_all_materials():
    materials = db.child("materials").get()
    if materials and materials.val():
        filtered_materials = [material for material in materials.val() if material and material.get("id") is not None]
        return filtered_materials if filtered_materials else []
    else:
        return []

def get_material(material_id):
    # Ejemplo: Obtener un usuario de la base de datos
    material = db.child("materials").child(material_id).get()
    return material.val()

def create_material(material_data):
    new_material = {
        "id": material_data["id"],
        "name": material_data["name"],
        "base_price": material_data["base_price"],
    }

    db.child("materials").child(new_material["id"]).set(new_material)
    return new_material

def update_material(material_id, updated_data):
    # Ejemplo: Actualizar un usuario en la base de datos
    material = get_material(material_id)
    if material:
        material.update(updated_data)
        db.child("materials").child(material_id).update(material)
        return material

def delete_material(material_id):
    # Ejemplo: Eliminar un usuario de la base de datos
    db.child("materials").child(material_id).remove()