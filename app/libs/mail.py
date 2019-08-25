"""
Created by Liangraorao on 2019/8/20 23:22
 __author__  : Liangraorao
filename : mail.py
"""
from app import mail
from flask_mail import Message
from flask import current_app, render_template


def send_mail(to, subject, template, **kwargs):
    msg = Message(subject='鱼书' + subject, sender=current_app.config[
        'MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)