from app.models import sale_model
from flask_restx import Namespace, Resource
from app.services.user_service import get_all_users, get_user, create_user, update_user, delete_user

api = Namespace('Sales', description='Users related operations')

user = api.model('Sales', sale_model)

@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users'''
        users = get_all_users()
        return users

    @api.doc('create_user')
    @api.expect(user)
    @api.marshal_with(user, code=201)
    def post(self):
        '''Create a new user'''
        new_user = create_user(api.payload)
        return new_user, 201

@api.route('/<int:id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        '''Fetch a user given its identifier'''
        user = get_user(id)
        if user:
            return user
        else:
            api.abort(404, "User not found")

    @api.doc('update_user')
    @api.expect(user)
    @api.marshal_with(user)
    def put(self, id):
        '''Update a user given its identifier'''
        updated_user = update_user(id, api.payload)
        if updated_user:
            return updated_user
        else:
            api.abort(404, "User not found")

    @api.doc('delete_user')
    @api.response(204, 'User deleted')
    def delete(self, id):
        '''Delete a user given its identifier'''
        delete_user(id)
        return '', 204