# app/apis/__init__.py
from flask import Blueprint
from flask_restx import Api

# Importar los namespaces
from .user import api as user_ns
from .sale import api as sale_ns
from .material import api as material_ns

# Crear un Blueprint para el API
api_blueprint = Blueprint('v1', __name__)

# Inicialización de la instancia de la clase Api
api = Api(
    api_blueprint,
    title='Hackathon 2024 API',
    version='1.0',
    description='The API designed for Optimization of requests, prices and route assignment for recyclers',
)

# Agregar los namespaces a la instancia de la clase Api
api.add_namespace(user_ns, path='/users')
api.add_namespace(sale_ns, path='/sales')
api.add_namespace(material_ns, path='/materials')
