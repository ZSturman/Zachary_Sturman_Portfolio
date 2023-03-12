import random
from datetime import datetime, date, timedelta
import secrets
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, current_app, abort
from flask_mail import Mail, Message
from config import get_settings
from app.main.models import Subscribers, db

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
    app.config['HOST'] = 'https://www.zsdynamics.com'
    mail.init_app(app)
    with app.app_context():
        current_app.mail = mail

def redirect_url(default='main.home'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@zs_mail.route('/already_subscribed', methods=['POST'])
def already_subscribed():
    set_subscribed(True)
    return redirect(redirect_url())

def set_subscribed(sub=False):
    session['subscribed'] = sub
    session.permanent = True
    return sub

@zs_mail.route("/usubscribe/<string:id>")
def unsubscribe(id):
    date = datetime.today()
    unsubscriber = Subscribers.query.filter_by(id=id).first()
    if not unsubscriber:
        abort(404)
    unsubscriber.updated = datetime.utcnow()
    unsubscriber.subscribed = False
    db.session.commit()
    set_subscribed(False)
    to_me(unsubscriber, "Unsubscribing")
    return render_template("mail/unsubscribe.html", title="Unsubscribe", person = unsubscriber, date=date)

@zs_mail.route("/unsubscribe_reason/<string:id>", methods=["GET", "POST"])
def unsubscribe_reason(id):
    date = datetime.today()
    person = Subscribers.query.filter_by(id=id).first()
    if not person:
        abort(404)
    if request.method == 'POST':
        if 'Send' in request.form:
            message = request.form['message']
            to_me(person, "Unsubscribe Reason", message)
        elif "No Answer" in request.form:
            message = person.name + "Do Not Want To Answer\n\n" + request.form['message']
            to_me(person, "Unsubscribe Reason", message)
        return render_template("mail/unsubscribe.html", title="Unsubscribe", person = person, date=date, sent=True)
    return redirect(redirect_url())
        

def to_me(person, subj, messg=None):
    date = datetime.today()
    msg = Message(
        subject = subj,
        recipients=[settings.MAIL_USERNAME],
        html = render_template("mail/to_me.html", title="To Me", person=person, message=messg, subject=subj, to_me = True, date=date)
    )
    current_app.mail.send(msg)







@zs_mail.route("/thanks_for_subscribing/<string:id>", methods=['GET', 'POST'])
def thanks_for_subscribing(id):
    date = datetime.today()
    subscriber = Subscribers.query.filter_by(id=id).first()
    if not subscriber:
        abort(404)
    subscriber.updated = datetime.utcnow()
    subscriber.subscribed = True
    if subscriber.welcome_basket_sent == False:
        unsubscribe_link = url_for('zs_mail.unsubscribe', id = subscriber.id, _external=True)
        msg = Message(
           subject = 'Welcome '+subscriber.name+"!",
           recipients= [subscriber.email],
           html = render_template("mail/welcome_basket.html", title="Thanks For Subscribing!", subscriber=subscriber, date=date,unsubscribe_link=unsubscribe_link)
       )
        current_app.mail.send(msg)
        subscriber.welcome_basket_sent = True
    db.session.commit()
    to_me(subscriber, "New Subscriber")
    set_subscribed(True)
    flash(f'You have successfully subscribed to ZSDynamics', 'success')
    return render_template('thanks_for_subscribing.html', title="Thanks For Subscribing!", person=subscriber, subscribing = True, date=date)


@zs_mail.route("/subscribe_frm_email/<string:id>", methods=["GET", "POST"])
def subscribe_frm_email(id):
    date = datetime.today()
    person = Subscribers.query.filter_by(id=id).first()
    if not person:
        abort(404)
    person.updated = datetime.utcnow()
    person.subscribed = True
    if person.welcome_basket_sent == False:
        unsubscribe_link = url_for('zs_mail.unsubscribe', id = person.id, _external=True)
        msg = Message(
           subject = 'Welcome '+person.name+"!",
           recipients= [person.email],
           html = render_template("mail/welcome_basket.html", title="Thanks For Subscribing!", person=person, date=date,unsubscribe_link=unsubscribe_link)
       )
        current_app.mail.send(msg)
        person.welcome_basket_sent = True
    db.session.commit()
    to_me(person, "New Subscriber")
    set_subscribed(True)
    flash(f'You have successfully subscribed to ZSDynamics', 'success')
    return render_template('thanks_for_subscribing.html', title="Thanks For Subscribing!", person=person, subscribing = True, date=date)

@zs_mail.route("/resubscribe/<string:id>", methods=["GET", "POST"])
def resubscribe(id):
    date = datetime.today()
    person = Subscribers.query.filter_by(id=id).first()
    if not person:
        abort(404)
    if person.subscribed == False:
        person.updated = datetime.utcnow()
        person.subscribed = True
        db.session.commit()
        to_me(person, "ReSubscriber")
        set_subscribed(True)
        flash(f'You have successfully resubscribed to ZSDynamics', 'success')
    return render_template('thanks_for_subscribing.html', title="Thanks For Subscribing!", person=person, subscribing = True, date=date, resubscribing=True)


@zs_mail.route('/subscribe', methods=["GET", "POST"])
def subscribe():
    name = request.form.get("new-subscribers-name")
    email = request.form.get("new-subscribers-email")
    if email is None or email == '':
        flash('Please enter a valid email', 'danger')
        return redirect(redirect_url())
    def to_emailer():
        date = datetime.today()
        subscriber = Subscribers.query.filter_by(email=email).first()
        if subscriber:
            subscriber.updated = datetime.utcnow()
            subscriber.subscribed = True
            if subscriber.name != name:
                subscriber.name = name
        else:
            subscriber = Subscribers(
                    name = name,
                    email = email,
                    subscribed = True,
                    created = datetime.utcnow(),
                    updated=datetime.utcnow()
                )
            db.session.add(subscriber)
        unsubscribe_link = url_for('zs_mail.unsubscribe', id = subscriber.id, _external=True)
        if subscriber.welcome_basket_sent == False:
            unsubscribe_link = url_for('zs_mail.unsubscribe', id = subscriber.id, _external=True)
            msg = Message(
               subject = 'Welcome '+subscriber.name+"!",
               recipients= [subscriber.email],
               html = render_template("mail/welcome_basket.html", title="Thanks For Subscribing!", person=subscriber, date=date,unsubscribe_link=unsubscribe_link)
            )    
            current_app.mail.send(msg)
            subscriber.welcome_basket_sent = True
        db.session.commit()
        to_me(subscriber, "New Subscriber")
    to_emailer()
    set_subscribed(True)
    flash(f'Check your email for your welcome basket', 'success')
    return redirect(redirect_url())



@zs_mail.route('/send_mail', methods=["GET", "POST"])
def send_mail():
    date = datetime.today()
    name = request.form.get("name")
    email = request.form.get("email")
    input_message = request.form.get("message")
    
    def to_emailer():
        emailer = Subscribers.query.filter_by(email=email).first()
        if emailer:
            emailer.updated = datetime.utcnow()
            if emailer.name != name:
                emailer.name = name
        else:
            emailer = Subscribers(
                name = name,
                email = email,
                subscribed = False,
                created = datetime.utcnow(),
                updated=datetime.utcnow()
            )
            db.session.add(emailer)
            db.session.commit()
        if emailer.last_email_sent and datetime.utcnow() - emailer.last_email_sent < timedelta(minutes=20):
            to_me(emailer, "Trying to send message within 'do not send window'")
        else:
            subscribe_link = url_for('zs_mail.subscribe_frm_email', id = emailer.id, _external=True)
            unsubscribe_link = url_for('zs_mail.unsubscribe', id = emailer.id, _external=True)
            msg = Message(
                    subject = 'Thanks for reaching out!',
                    recipients= [email,settings.MAIL_USERNAME],
                    html = render_template("mail/thanks_for_reaching_out.html", person=emailer, reaching_out=True, date=date, subscribe_link=subscribe_link, unsubscribe_link=unsubscribe_link)
                )
            current_app.mail.send(msg)
            emailer.last_email_sent = datetime.utcnow()
            db.session.commit()
        to_me(emailer, "New Message", input_message)
        
    to_emailer()
    flash(f"Thanks for reaching out! A reply will be sent to your email soon", 'success')
    return redirect(redirect_url())


@zs_mail.route("/news_letter")
def news_letter():
    return render_template("mail/news_letter.html", title="News Letter")




@zs_mail.route("/test_mail_page")
def testing_mail_page():
    date = datetime.today()
    
    person = Subscribers(
        name = "Test P. Tester",
        email = "test@test.com",
        subscribed = False,
        created = datetime.utcnow(),
        updated = datetime.utcnow()
    )
    subscribe_link = url_for('zs_mail.subscribe', id = person.id, _external=True)
    unsubscribe_link = url_for('zs_mail.unsubscribe', id = person.id, _external=True)
    return render_template("mail/thanks_for_reaching_out.html", person=person, date=date, subscribe_link=subscribe_link, unsubscribe_link=unsubscribe_link)