# from app.form.auth import RegisterForm, LoginForm
from app.model.user import User
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from . import web
from flask import render_template, request, redirect, url_for, flash
from app.model.base import db
from flask_login import login_user, login_required, logout_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_to_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
            return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                return redirect(url_for('web.index'))
            return redirect(next)
        else:
            flash('用户不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first_or_404()
        if user:
            from app.libs.mail import send_mail
            send_mail(form.email.data, '重置你的密码', 'email/reset_password.html', user=user, token=user.generate_token())
    return render_template('/auth/forget_password_request.html')


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash('你的密码已更新，请使用新密码登录')
            return redirect(url_for('web.login'))
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
