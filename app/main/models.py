""" from datetime import datetime
import secrets
from app import db

class Subscribers(db.Model):
    id = db.Column(db.String(32), primary_key=True, default=secrets.token_urlsafe)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    subscribed = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    welcome_basket_sent = db.Column(db.Boolean, default=False)
    last_email_sent = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Subscribers(name='{self.name}', email='{self.email}', subscribed='{self.subscribed}', created='{self.created}', updated='{self.updated}')>"
 """