from application import db
from application.models import Base

class Task(Base):
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(2000), nullable = False)
    tests = db.Column(db.String(500), nullable = False)
    submits = db.relationship("Submit", backref = "task", lazy = True)

    def __init__(self, title, description, tests):
        self.title = title
        self.description = description
        self.tests = tests

class Submit(Base):
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable = False, index = True)
    grammar = db.Column(db.String(1000), nullable = False)
    success = db.Column(db.Boolean, nullable = False)

    def __init__(self, task_id, grammar, success):
        self.task_id = task_id
        self.grammar = grammar
        self.success = success
