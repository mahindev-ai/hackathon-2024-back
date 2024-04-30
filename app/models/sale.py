from flask_restx import fields
from app.apis.material import user as material
from app.apis.user import user
sale_model = {
    'id': fields.String(description='ID del usuario'),
    'seller': fields.Nested(user, description='Vendedor del material'),
    'buyer': fields.Nested(user, description='Comprador del material'),
    'material': fields.Nested(material, description='Material a vender'),
    'amount': fields.String(description='Cantidad de material a vender'),
    'price': fields.Integer(description='Precio final'),
}