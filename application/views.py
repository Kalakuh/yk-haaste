from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html", tasks = Task.query.all()[::-1])

@app.route("/404/")
def error404():
	return render_template("404.html")

@app.errorhandler(500)
def on500(e):
	return render_template("404.html")

@app.errorhandler(404)
def on404(e):
	return render_template("404.html")