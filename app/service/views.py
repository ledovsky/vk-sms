from flask import Blueprint, render_template, request
from .models import Group

mod = Blueprint('service', __name__, url_prefix='/service')


@mod.route('/')
def dashboard():
    return render_template('service/dashboard.html')


@mod.route('/groups')
def groups():
    active_groups = Group.query.filter_by(active=True).all()
    non_active_groups = Group.query.filter_by(active=False).all()
    print '123'
    return render_template('service/groups.html', non_active_groups=non_active_groups)


@mod.route('/groups/edit/<group_id>')
def edit_group(group_id):
    pass


@mod.route('stats')
def stats():
    pass


@mod.route('payment')
def payment():
    pass