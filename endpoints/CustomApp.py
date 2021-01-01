from flask import request
from flask_restplus import Resource, fields
from endpoints.restapi import api

ns = api.namespace('CustomApp', description='Custom operations')
custom_request_dto = api.model('CustomReqDto', {
    'year': fields.String(required=True, description='Year details'),
    'month': fields.String(required=False, description='Month task details')
})


@ns.route('/api/v1/')
class CustomGet(Resource):
    @api.doc(responses={200: 'OK'})
    @ns.response(204, 'Todo deleted')
    @ns.doc('CustomGet')
    def get(self):
        """Get with no query param"""
        return "Custom app"


@ns.route('/api/v1/<mobile>')
@api.doc(params={'mobile': {'description': 'mobile number is required'},
                 'address': {'description': 'address is optional', 'default': None}})
class MyResource(Resource):
    @api.doc(responses={200: 'OK'})
    @ns.response(204, 'Todo deleted')
    @ns.doc('CustomGet with query param')
    def get(self, mobile):
        """Get with one required & 1 query param"""
        address = request.args.get('address')
        return {'mobile': mobile, 'address': address}

    @api.doc(params={'email': {'description': 'email is optional'}})
    def post(self, mobile):
        """Post with one required & 2 query param"""
        email = request.args.get('email')
        address = request.args.get('address')
        return {'mobile': mobile, 'address': address, 'email': email}
