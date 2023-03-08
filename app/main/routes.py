from flask import Blueprint, render_template, url_for

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", title="Zachary Sturman")

@main.route("/about")
def about():
    return render_template("about.html", title="About")

@main.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@main.route("/tester_page")
def testing_page():
    return render_template("testing_page.html")

