
import random
from datetime import datetime, date, timedelta
import secrets
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, current_app, abort
from flask_mail import Mail, Message
from config import get_settings

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
    app.config['MAIL_ASCII_ATTACHMENTS'] = True

    app.config['HOST'] = 'https://www.zsdynamics.com'
    mail.init_app(app)
    with app.app_context():
        current_app.mail = mail

def msg_attachments(msg, welcome_basket=False):
    msg.attach('githubicon.png','image/png',open('app/static/images/githubicon.png', 'rb').read(), 'inline', headers=[['Content-ID','<Mailgithub>'],])
    msg.attach('linkedinicon.png','image/png',open('app/static/images/linkedinicon.png', 'rb').read(), 'inline', headers=[['Content-ID','<Maillinkedin>'],])
    msg.attach('twittericon.png','image/png',open('app/static/images/twittericon.png', 'rb').read(), 'inline', headers=[['Content-ID','<Mailtwitter>'],])
    msg.attach('emailbanner_logo.png','image/png',open('app/static/images/emailbanner_logo.png', 'rb').read(), 'inline', headers=[['Content-ID','<Emailbanner>'],])
    msg.attach('zssignature.png','image/png',open('app/static/images/zssignature.png', 'rb').read(), 'inline', headers=[['Content-ID','<Signature>'],])
    if welcome_basket == True:
        msg.attach('mail_tips.png','image/png',open('app/static/images/mail_tips.png', 'rb').read(), 'inline', headers=[['Content-ID','<MailTips>'],])
        msg.attach('mail_science.png','image/png',open('app/static/images/mail_science.png', 'rb').read(), 'inline', headers=[['Content-ID','<MailScience>'],])
        msg.attach('mail_project.png','image/png',open('app/static/images/mail_project.png', 'rb').read(), 'inline', headers=[['Content-ID','<MailProject>'],])
        msg.attach('mail_learn.png','image/png',open('app/static/images/mail_learn.png', 'rb').read(), 'inline', headers=[['Content-ID','<MailLearn>'],])
        msg.attach('mail_flame.png','image/png',open('app/static/images/mail_flame.png', 'rb').read(), 'inline', headers=[['Content-ID','<MailFlame>'],])

def redirect_url(default='main.home'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


def to_me(person, subj, messg=None):
    date = datetime.today()
    msg = Message(
        subject = subj,
        recipients=[settings.MAIL_USERNAME],
        html = render_template("mail/to_me.html", title="To Me", person=person, message=messg, subject=subj, to_me = True, date=date)
    )
    msg_attachments(msg)
    current_app.mail.send(msg)




@zs_mail.route('/send_mail', methods=["GET", "POST"])
def send_mail():
    honeypot_email = request.form.get("honeypot_email")
    honeypot_name = request.form.get("honeypot_name")
    if honeypot_email:
        flash('Mail not accepted.', 'danger')
        return redirect(redirect_url())
    if honeypot_name:
        flash('Mail not accepted.', 'danger')
        return redirect(redirect_url())
    date = datetime.today()
    name = request.form.get("name")
    email = request.form.get("email")
    input_message = request.form.get("message")

    person = {'name': name, 'email': email}

    msg = Message(
            subject = 'Thanks for reaching out!',
            recipients= [email, settings.MAIL_USERNAME],
            html = render_template("mail/thanks_for_reaching_out.html", reaching_out=True, date=date, person=person)
        )
    msg_attachments(msg)
    current_app.mail.send(msg)
    to_me(name, "New Message", input_message)

    flash(f"Thanks for reaching out! A reply will be sent to your email soon", 'success')
    return redirect(redirect_url())
