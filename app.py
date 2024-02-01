from flask import Flask
from controller.TaskController import todoroute
from models.TaskModel import db

app  = Flask(__name__)

app.config['MONGODB_SETTINGS']={
    "host": "mongodb://127.0.0.1/tododb"
}

db.init_app(app)

app.register_blueprint(todoroute)



if __name__ == "__main__":
    app.run(debug=True)