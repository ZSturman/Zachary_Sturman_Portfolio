from flask import Blueprint, render_template, url_for

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")
