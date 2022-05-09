from flask import Blueprint, request, redirect, session
from flask import render_template, g, Blueprint
from api.user_api import User, UserDB

user_list_blueprint = Blueprint('user_list_blueprint', __name__)

@user_list_blueprint.route('/signup', methods = ['GET', 'POST'])
def signup():
    database = UserDB(g.mysql_db, g.mysql_cursor)

    if request.method == "POST":
        username = request.form('username')
        password = request.form('password')

        if database.select_user_by_username(username):
            msg = 'Username has already been taken'
        elif not username or not password:
            msg = 'Please enter a username AND password'
        else:
            new_user = User(username, password)
            database.insert_user(new_user)
            msg = 'Account creation successful'

    return render_template('signup.html', msg = msg)


@user_list_blueprint.route('/login', methods =['GET', 'POST'])
def login():
    database = UserDB(g.mysql_dp, g.mysql_cursor)

    if request.method == "POST":
        username = request.form('username')
        password = request.form('password')

        user = database.select_user_by_username(username)
        if user == database.select_user_by_password(password):
            session['loggedin'] = True
            session['id'] = user['user_id']
            session['username'] = user['username']
            msg = 'Login successful'
        else:
            msg = 'Wrong username or password'

    return render_template('login.html', msg = msg)