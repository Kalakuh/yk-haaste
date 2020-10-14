from flask import render_template, request, redirect, url_for

from application import app, db
from application.tasks.models import Task, Submit

@app.route("/task/<task_id>/")
def handle_task(task_id):
	task = Task.query.get(task_id)
	tests = task.tests.split("\n")
	valid = [test[1:] for test in tests if test[0] == '+']
	invalid = [test[1:] for test in tests if test[0] == '-']
	if request.method == "GET":
		return render_template("tasks/task.html", task=task, valid=valid, invalid=invalid, grammar="")
	
	grammar = request.form["grammar"]
	return render_template("tasks/task.html", task=task, valid=valid, invalid=invalid, grammar=grammar)

@app.route("/task/new/", methods = ["GET", "POST"])
def new_task():
	if request.method == "GET":
		return render_template("tasks/new.html")
	
	task = Task(request.form["title"], request.form["desc"], request.form["tests"])
	db.session().add(task)
	db.session().commit()

	return redirect(url_for("index"))