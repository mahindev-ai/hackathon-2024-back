from flask_restx import fields

material_model = {
    'id': fields.String(description='ID del material en la base de datos'),
    'name': fields.String(description='Nombre del material'),
    'base_price': fields.String(description='Precio promedio de los materiales'),
}