from flask_mongoengine import Mongoengine


db = Mongoengine()


class Todo(db.Document):
     name = db.StringField(required=True,max_length=200)
     description = db.StringField()
     done = db.BooleanField(default=False)


     