from app.models.material import material_model
from flask_restx import Namespace, Resource
from app.services.material_service import get_all_materials, get_material, create_material, update_material, delete_material

api = Namespace('Materials', description='Mgitaterials related operations')

material = api.model('Materials', material_model)

@api.route('/')
class materialList(Resource):
    @api.doc('list_materials')
    @api.marshal_list_with(material)
    def get(self):
        '''List all materials'''
        materials = get_all_materials()
        return materials

    @api.doc('create_material')
    @api.expect(material)
    @api.marshal_with(material, code=201)
    def post(self):
        '''Create a new material'''
        new_material = create_material(api.payload)
        return new_material, 201

@api.route('/<int:id>')
@api.param('id', 'The material identifier')
@api.response(404, 'material not found')
class Material(Resource):
    @api.doc('get_material')
    @api.marshal_with(material)
    def get(self, id):
        '''Fetch a material given its identifier'''
        material = get_material(id)
        if material:
            return material
        else:
            api.abort(404, "material not found")

    @api.doc('update_material')
    @api.expect(material)
    @api.marshal_with(material)
    def put(self, id):
        '''Update a material given its identifier'''
        updated_material = update_material(id, api.payload)
        if updated_material:
            return updated_material
        else:
            api.abort(404, "material not found")

    @api.doc('delete_material')
    @api.response(204, 'material deleted')
    def delete(self, id):
        '''Delete a material given its identifier'''
        delete_material(id)
        return '', 204