from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)

from main.views import mod as mainModule
from service.views import mod as serviceModule

app.register_blueprint(mainModule)
app.register_blueprint(serviceModule)
