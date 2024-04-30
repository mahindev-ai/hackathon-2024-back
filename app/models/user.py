from flask_restx import fields

user_model = {
    'id': fields.String(description='ID del usuario'),
    'name': fields.String(description='Nombre del usuario'),
    'email': fields.String(description='Correo de usuario'),
    'password': fields.String(description='Contraseña del usuario'),
    'address': fields.String(description='Dirección del usuario para determinar las zonas cercanas'),
    'role': fields.Integer(description='ID del rol del usuario', default=1),
    'role_name': fields.String(description='Nombre del rol del usuario (reciclador o vendedor)', required=False, default= 'Vendedor')
}