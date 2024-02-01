from flask import Blueprint,request
from models.TaskModel import Todo


todoroute = Blueprint("todoroute",__name__, url_prefix="/api/v1")


@todoroute.post("/createtodo")
def createTodo():
    todo_post = request.json()

    newtodo = Todo(name = todo_post["name"], description = todo_post["desc"])
    newtodo.save()

    return {"message":"Created Successfully","data":newtodo}

@todoroute.post("/editTodo/<id>")
def editTodo(id):
    todo_update = request.json()
    todo = Todo.objects.get_or_404(id=id)

    if not todo:
        return "User"f"{todo.id}""not found"
    else:
        todo.name = todo_update.get("name", todo.name)
        todo.description = todo_update.get("desc", todo.description)
        todo.save()

    return {"message":"Updated Successfully", "data":todo}

