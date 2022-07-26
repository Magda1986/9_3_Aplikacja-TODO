import json


class Todos:
    def __init__(self):
        try:
            with open("todos.json", "r") as f:
                self.todos = json.load(f)
            self.next_id = self.todos.pop("next_id")
        except FileNotFoundError:
            self.todos = {}
            self.next_id = 1

    def all(self):
        return self.todos

    def get(self, id: str) -> dict:
        return self.todos.get(id)

    def create(self, data: dict) -> None:
        #data.pop("csrf_token")
        self.todos[self.next_id] = data
        self.next_id += 1
        self.save_all()

    def update(self, id: str, data: dict) -> bool:
        #data.pop("csrf_token")
        if id not in self.todos:
            return False
        self.todos[id] = data
        self.save_all()
        return True

    def delete(self, id: str) -> bool:
        todo = self.todos.pop(id, None)
        if todo:
            self.save_all()
            return True
        return False

    def save_all(self):
        dict_to_save = self.todos.copy()
        dict_to_save["next_id"] = self.next_id

        with open("todos.json", "w") as f:
            json.dump(dict_to_save, f)


todos = Todos()


# print(todos.get("44"))

#print(todos.all())
#todos.create(
#     {
#         "csrf_token": "kkk",
#         "title": "ekler",
#         "description": "Krem, ciasto francuskie",
#         "done": False,
#     }
# )
