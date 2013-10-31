from flask import Blueprint, session, redirect

mod = Blueprint('service', __name__, url_prefix='/service')


@mod.route("/login", methods=["GET", "POST"])
def login():
    session['user_id'] = 1
    return redirect('service.dashboard')
