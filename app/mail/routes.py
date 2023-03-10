import random
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, current_app
from flask_mail import Mail, Message
from itsdangerous import URLSafeSerializer, BadData
from config import get_settings
import pandas

zs_mail = Blueprint("zs_mail", __name__)

settings = get_settings()

@zs_mail.record
def record(state):
    app = state.app
    mail = Mail()
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEBUG'] = True
    app.config['MAIL_DEFAULT_SENDER'] = ("Zachary from ZSDynamics.com", "ZS@ZSDynamics.com")
    app.config['MAIL_MAX_EMAILS'] = 5
    app.config['MAIL_USERNAME'] = settings.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = settings.MAIL_PASSWORD
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    app.config['SUBSCRIBERS_LIST'] = settings.SUBSCRIBERS_LIST
    mail.init_app(app)
    with app.app_context():
        current_app.mail = mail



@zs_mail.route("/thanks_for_subscribing/<name>/<email>", methods=['GET', 'POST'])
def thanks_for_subscribing(name, email):
    set_subscribed(True)
    add_subscriber(name, email)
    flash(f'You have successfully subscribed to ZSDynamics', 'success')
    return render_template('mail/thanks_for_subscribing.html', title="Thanks For Subscribing!", name=name, email=email)


@zs_mail.route('/already_subscribed', methods=['POST'])
def already_subscribed():
    set_subscribed(True)
    return redirect(redirect_url())

@zs_mail.route('/subscribe', methods=["GET", "POST"])
def subscribe():
    name = request.form.get("new-subscribers-name")
    email = request.form.get("new-subscribers-email")
    if email is None or email == '':
        flash('Please enter a valid email', 'danger')
        return redirect(redirect_url())
    msg = Message(
        subject = 'Welcome '+name+"!",
        recipients= [email],
        html = render_template("mail/welcome_basket.html", name=name, email=email)
    )
    add_subscriber(name, email)
    current_app.mail.send(msg)
    set_subscribed(True)
    flash(f'Check your email for your welcome basket', 'success')
    return redirect(redirect_url())


@zs_mail.route('/send_mail', methods=["GET", "POST"])
def send_mail():
    name = request.form.get("name")
    email = request.form.get("email")
    input_message = request.form.get("message")

    def to_emailer():
        if email in current_app.config['SUBSCRIBERS_LIST']:
            msg = Message(
                subject = 'Thanks for reaching out!',
                recipients= [email, "zacharysturman@zsdynamics.com"],
                html = render_template("mail/thanks_for_reaching_out_subsd.html", name=name, input_message=input_message, email=email)
            )
        else:
            msg = Message(
                subject = 'Thanks for reaching out!',
                recipients= [email, "zacharysturman@zsdynamics.com"],
                html = render_template("mail/thanks_for_reaching_out.html", name=name, input_message=input_message, email=email)
            )
        current_app.mail.send(msg)
            
    def to_me():
        msg = Message(
            subject = 'To Me',
            recipients= ["zacharysturman@zsdynamics.com"],
            html = "from: "+name+" email: "+email+" message: "+input_message
        )
        current_app.mail.send(msg)
    
    to_emailer()
    to_me()
    flash(f"Thanks for reaching out! A reply will be sent to your email soon", 'success')

    return redirect(redirect_url())

def redirect_url(default='home'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

def add_subscriber(name, email):
    if name == None:
        name = "Name is None"
    if email == None:
        email = "Email is None" 
    msg = Message(
        subject = 'New Subscriber',
        recipients= ["zasturman@gmail.com", "zacharysturman@zsdynamics.com"],
        body = name +" "+ email
    )
    current_app.mail.send(msg)
    set_subscribed()

def set_subscribed(sub=False):
    session['subscribed'] = sub
    session.permanent = True
    return sub

@zs_mail.route("/usubscribe/<string:name>/<string:email>")
def unsubscribe(name, email):
    set_subscribed(False)
    remove_subscriber(name, email)
    return render_template("mail/unsubscribe.html", title="Unsubscribe")


def remove_subscriber(name, email):
    msg = Message(
        subject = 'Remove Subscriber: '+name,
        recipients= ["zasturman@gmail.com", "zacharysturman@zsdynamics.com"],
        body = "name:"+name+"\n\nemail: "+email
    )
    current_app.mail.send(msg)

