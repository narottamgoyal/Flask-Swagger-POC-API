from flask_restplus import Api, Resource, fields
from TodoDto import TodoDto
from endpoints.restapi import api

ns = api.namespace('TodoApp', description='Todo operations')

todoRequestDto = api.model('TodoReqDto', {
    'task_name': fields.String(required=True, description='The task details')
})

todoResponseDto = api.model('TodoResponseDto', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task_name': fields.String(required=True, description='The task details')
})

todo_list = TodoDto()
todo_list.create({'task_name': 'Build an API'})
todo_list.create({'task_name': '?????'})
todo_list.create({'task_name': 'profit!'})


@ns.route('/api/v1/')
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @ns.doc('list_todos')
    @ns.marshal_list_with(todoResponseDto)
    def get(self):
        """List all tasks"""
        return todo_list.todos

    @ns.doc('create_todo')
    @ns.expect(todoRequestDto)
    @ns.marshal_with(todoResponseDto, code=201)
    def post(self):
        """Create a new task"""
        return todo_list.create(api.payload), 201


@ns.route('/api/v1/<int:task_id>')
@ns.response(404, 'Todo not found')
@ns.param('task_id', 'The task identifier')
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @ns.doc('get_todo')
    @ns.marshal_with(todoResponseDto)
    def get(self, task_id):
        """Fetch a given resource"""
        result = todo_list.get(task_id)
        if result is None:
            api.abort(404, "Todo {} doesn't exist".format(task_id))
        else:
            return result

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, task_id):
        """Delete a task given its identifier"""
        todo_list.delete(task_id)
        return '', 204

    @ns.expect(todoRequestDto)
    @ns.marshal_with(todoResponseDto)
    def put(self, task_id):
        """"Update a task given its identifier"""
        result = todo_list.update(task_id, api.payload)
        if result is None:
            api.abort(404, "Todo {} doesn't exist".format(task_id))
        else:
            return result
