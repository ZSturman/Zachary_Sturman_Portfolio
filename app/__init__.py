import random
from flask import Flask, session
from flask_mail import Mail, Message
from app.context_processors import portfolio_context_processor
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    mail = Mail()
    mail.init_app(app)

    app.context_processor(lambda: portfolio_context_processor(config_class))

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