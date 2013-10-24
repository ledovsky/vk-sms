from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app.main.views import mod as mainModule
from app.service.views import mod as serviceModule

app.register_blueprint(mainModule)
app.register_blueprint(serviceModule)
