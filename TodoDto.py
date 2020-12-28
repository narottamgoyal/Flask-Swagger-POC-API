import time


class TodoDto(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, task_id):
        for todo in self.todos:
            if todo['id'] == task_id:
                return todo
        return None

    def create(self, todo):
        todo = todo
        todo['id'] = int(time.perf_counter())
        self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, task_id, data):
        todo = self.get(task_id)
        if todo is not None:
            todo.update(data)
        return todo

    def delete(self, task_id):
        todo = self.get(task_id)
        self.todos.remove(todo)
