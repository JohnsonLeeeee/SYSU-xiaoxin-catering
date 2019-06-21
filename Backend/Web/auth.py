from flask import render_template, redirect, Blueprint, g
from flask import request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user

from ..Form.Auth_admin import RegisterForm, LoginForm, ResetPasswordForm, EmailForm, \
    ChangePasswordForm
from ..Model.administrator import Adminstrator
from ..Model.restaurant import Restaurant
from ..Model.base import db
from ..libs.email import send_email


web = Blueprint( 'web',__name__ )

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Adminstrator()
        user.set_attrs(form.data)
        res = Restaurant.query.filter_by(id=form.restaurant.data).first()
        user.restaurant = res
        with db.auto_commit():
            db.session.add(user)
        # token = user.generate_confirmation_token()
        # send_email(user.email, 'Confirm Your Account',
        #            'email/confirm', user=user, token=token)
        login_user(user, False)
        # flash('一封激活邮件已发送至您的邮箱，请快完成验证', 'confirm')
        # 由于发送的是ajax请求，所以redirect是无效的
        # return render_template('index.html')
        return redirect(url_for('index.index'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Adminstrator.query.filter_by(email=form.email.data).first()
        if user and user.check_pwd(form.password.data):
            login_user(user, remember=True)
            if current_user not in g:
                g.current_user = user
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('index.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误', category='login_error')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    if request.method == 'POST':
        form = EmailForm(request.form)
        if form.validate():
            account_email = form.email.data
            user = Adminstrator.query.filter_by(email=account_email).first_or_404()
            send_email(form.email.data, '重置你的密码',
                       'email/reset_password', user=user,
                       token=user.generate_token())
            flash('一封邮件已发送到邮箱' + account_email + '，请及时查收')
            return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html')


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    if not current_user.is_anonymous:
        return redirect(url_for('web.index'))
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        result = Adminstrator.reset_password(token, form.password1.data)
        if result:
            flash('你的密码已更新,请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            return redirect(url_for('web.index'))
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        current_user.password = form.new_password1.data
        db.session.commit()
        flash('密码已更新成功')
        return redirect(url_for('web.personal'))
    return render_template('auth/change_password.html', form=form)


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        form = RegisterForm()
        form.validate()
        user = Adminstrator()
        user.set_attrs(form.data)
        res = Restaurant.query.filter_by(id = form.restaurant.data).first()
        user.restaurant = res
        with db.auto_commit():
            db.session.add(user)
        # token = user.generate_confirmation_token()
        # send_email(user.email, 'Confirm Your Account',
        #            'email/confirm', user=user, token=token)
        login_user(user, False)
        g.status = True
        flash('一封激活邮件已发送至您的邮箱，请快完成验证', 'confirm')
        # 由于发送的是ajax请求，所以redirect是无效的
        return 'go to index'


