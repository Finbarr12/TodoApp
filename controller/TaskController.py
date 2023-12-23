from flask import Blueprint,request
from ..models.TaskModel import Todo


todoroute = Blueprint("todoroute",__name__, url_prefix="/api/v1")


@todoroute.post("/createtodo")
def createTodo():
    todo_post = request.get_json()

    newtodo = Todo(name = todo_post["name"], description = todo_post["desc"])
    newtodo.save()

    return {"message":"Created Successfully","data":newtodo}