from app.models.sale import sale_model
from flask_restx import Namespace, Resource
from app.services.sale_service import get_all_sales, get_sale, create_sale, update_sale, delete_sale

api = Namespace('Sales', description='Sales related operations')

sale = api.model('Sales', sale_model)

@api.route('/')
class SaleList(Resource):
    @api.doc('list_sales')
    @api.marshal_list_with(sale)
    def get(self):
        '''List all sales'''
        sales = get_all_sales()
        return sales

    @api.doc('create_sale')
    @api.expect(sale)
    @api.marshal_with(sale, code=201)
    def post(self):
        '''Create a new sale'''
        new_sale = create_sale(api.payload)
        return new_sale, 201

@api.route('/<int:id>')
@api.param('id', 'The sale identifier')
@api.response(404, 'sale not found')
class Sale(Resource):
    @api.doc('get_sale')
    @api.marshal_with(sale)
    def get(self, id):
        '''Fetch a sale given its identifier'''
        sale = get_sale(id)
        if sale:
            return sale
        else:
            api.abort(404, "sale not found")

    @api.doc('update_sale')
    @api.expect(sale)
    @api.marshal_with(sale)
    def put(self, id):
        '''Update a sale given its identifier'''
        updated_sale = update_sale(id, api.payload)
        if updated_sale:
            return updated_sale
        else:
            api.abort(404, "sale not found")

    @api.doc('delete_sale')
    @api.response(204, 'sale deleted')
    def delete(self, id):
        '''Delete a sale given its identifier'''
        delete_sale(id)
        return '', 204