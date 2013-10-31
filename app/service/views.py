from flask import Blueprint, render_template, request

mod = Blueprint('service', __name__, url_prefix='/service')


@mod.route('/')
def dashboard():
    return render_template('service/dashboard.html')


@mod.route('/groups')
def groups():
    pass


@mod.route('/groups/edit/<group_id>')
def edit_group(group_id):
    pass


@mod.route('stats')
def stats():
    pass


@mod.route('payment')
def payment():
    pass