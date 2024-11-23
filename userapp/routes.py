from flask import request, jsonify, render_template, redirect, url_for, flash, Blueprint

users = Blueprint(name='users', import_name='app.users.routes', template_folder='templates', static_folder='static')

@users.route('/')
def dashboard_view():
    return render_template('users/dashboard.html')

@users.route('/signin')
def signin_view():
    return render_template('users/signin.html')
