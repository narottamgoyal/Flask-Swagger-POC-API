from flask_restplus import Resource
from endpoints.restplus import api

ns = api.namespace('CustomApp', description='Custom operations')


@ns.route('/api/v1/')
class CustomTodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    # @api.doc(responses={200: 'OK'})
    # @ns.marshal_list_with()
    @ns.doc('custom_list_todos')
    def get(self):
        # """List all tasks"""
        return "Custom app"
