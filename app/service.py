from modelsMongo import ToDoModel


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params)

    def list(self):
        response = self.model.list_items()
        return response