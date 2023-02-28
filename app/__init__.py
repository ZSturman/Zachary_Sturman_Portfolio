from flask import Flask
from flask_mail import Mail, Message


def create_app():
    app = Flask(__name__)

    mail = Mail()
    mail.init_app(app)

    from app.errors.handlers import errors
    from app.main.routes import main
    from app.projects.routes import projects
    from app.services.routes import services
    from app.mail.routes import zs_mail
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(projects)
    app.register_blueprint(services)
    app.register_blueprint(zs_mail)

    return app