from flask import Blueprint, render_template

mod = Blueprint('main', __name__, url_prefix='')


@mod.route('/')
def main_page():
    return render_template('main/main_page.html')
