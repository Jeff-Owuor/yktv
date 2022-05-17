from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
import smtplib
import os

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Jeff's blog login"
    return render_template('auth/login.html',login_form = login_form,title=title)



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User(email = email, username = form.username.data,password = form.password.data)
        
        message = "You have been subscribed to Day in the life.. application"
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("Xjeff37@gmail.com",os.environ.get('MAIL_PASSWORD'))
        server.sendmail("Xjeff37@gmail.com",email,message)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/registration.html',registration_form = form)