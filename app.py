from flask import Flask, abort, jsonify, make_response, request
from models import todos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/todos/", methods=["GET"])
def todos_list_api_v1():
    return jsonify(todos.all())


@app.route("/api/v1/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todos.get(str(todo_id))
    if not todo:
        abort(404)
    return jsonify({"todo": todo})

@app.route("/api/v1/todos/<int:todo_id>", methods=['DELETE'])
def delete_todo(todo_id):
    result = todos.delete(str(todo_id))
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "not_found", "status_code": 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@app.route("/api/v1/todos/", methods=["POST"])
def create_todo():
    if (
        not request.json
        or not "title" in request.json
        or not "description" in request.json
        or not "done" in request.json
    ):
        abort(400)
    todo = {
        "title": request.json["title"],
        "description": request.json["description"],
        "done": request.json["done"],
    }
    todos.create(todo)
    return jsonify({"todo": todo}), 201

@app.route("/api/v1/todos/<int:todo_id>", methods=['PUT'])
def update_todo(todo_id):
    if str(todo_id) not in todos.all():
        abort(404)
    if (
        not request.json
        or not "title" in request.json
        or not "description" in request.json
        or not "done" in request.json
    ):
        abort(400)
    todo = {
        "title": request.json["title"],
        "description": request.json["description"],
        "done": request.json["done"],
    }
    todos.update(str(todo_id), todo)
    return jsonify({"todo": todo})

if __name__ == "__main__":
    app.run(debug=True)
