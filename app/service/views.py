from flask import Blueprint, render_template, request

mod = Blueprint('service', __name__, url_prefix='/service')

@mod.route('')
def test_service():
    return 