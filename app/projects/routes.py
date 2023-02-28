from flask import Blueprint, render_template

projects = Blueprint("projects", __name__)

@projects.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")