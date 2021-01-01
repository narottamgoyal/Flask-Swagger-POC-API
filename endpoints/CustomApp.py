from flask import request
from flask_restplus import Resource
from endpoints.restapi import api

ns = api.namespace('CustomApp', description='Custom operations')


@ns.route('/api/v1/')
class CustomGet(Resource):
    @api.doc(responses={200: 'OK'})
    @ns.response(204, 'No Content')
    @ns.doc('CustomGet')
    def get(self):
        """Simple Get with no param"""
        return "Custom app"


@ns.route('/api/v1/<mobile>')
@api.doc(params={'mobile': {'description': 'mobile number is required'},
                 'address': {'description': 'address is optional', 'default': None}})
class MyResource(Resource):

    @api.doc(responses={200: 'OK'})
    @ns.response(204, 'No Content')
    @ns.doc('CustomGet with query param')
    def get(self, mobile):
        """Get with one required & 1 query param"""
        address = request.args.get('address')
        return {'mobile': mobile, 'address': address}

    @api.doc(params={'email': {'description': 'email is optional', 'default': 'default@email.com'}})
    def post(self, mobile):
        """Post with one required & 2 query param"""
        email = request.args.get('email')
        address = request.args.get('address')
        return {'mobile': mobile, 'address': address, 'email': email}

    @ns.doc('custom delete')
    @ns.response(204, 'deleted')
    def delete(self, mobile):
        """Delete with mobile number"""
        return {'mobile': mobile}

    @ns.response(204, 'updated')
    @ns.doc('custom update')
    def put(self, mobile):
        """"Update with mobile number"""
        return {'mobile': mobile}
