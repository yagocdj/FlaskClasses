# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from puppyCompanyBlog import db
from puppyCompanyBlog.models import User, BlogPost
from puppyCompanyBlog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppyCompanyBlog.users.picture_handler import add_profile_pick
from time import sleep

users = Blueprint('users', __name__)

# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        # sleep(1)
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

# login
@users.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)
             

# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

# account (update UserForm)
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    
    form = UpdateUserForm()

    if form.validate_on_submit():
        
        if form.pic.data:
            username = current_user.username
            pic = add_profile_pick(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User account updated')
        return redirect(url_for('users.account'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)

# user's list of blog posts