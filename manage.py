import datetime

from flask.ext.script import Manager

from app import app
from app import db
from app.users.models import User
from app.test_db_data.utils import fill_database

manager = Manager(app)
app.config.from_object('config')


@manager.command
def run():
    app.run()


@manager.command
def test():
    print 'hello world'


@manager.command
def create_test_user():
    user = User()
    user.vk_id = "24076752"
    user.access_token = "GsPlUf1RVH8AAAAAAAAAAQIpLzXXVtywxpD90ySk8XbSsFO5DoU0dhOlGU4qU5Fc"
    user.expires = datetime.datetime.now() + datetime.timedelta(days=100)
    db.session.add(user)
    db.session.commit()


@manager.command
def create_all():
    db.create_all()


@manager.command
def fill_db():
    fill_database()


if __name__ == '__main__':
    manager.run()
