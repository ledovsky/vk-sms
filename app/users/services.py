from flask import session, redirect
from app import app
from .models import User


def get_user_id():
    if 'user_id' in session:
        return session['user_id']
    else:
        return None


def logout():
    session['user_id'] = None


def login_required(func):
    def wrapper(*args, **kwargs):
        if not get_user_id():
            return redirect('users.login_page')
        user = User.query.get(id=get_user_id())
        if user.is_expired():
            logout()
            return redirect('users.login_page')
        return func(*args, **kwargs)
    return wrapper

