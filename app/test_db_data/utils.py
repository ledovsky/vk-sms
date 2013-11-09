import json

from app import db
from app.service.models import Group, Number


def fill_database():
    # f = open("app/test_db_data/groups.json")
    # data = json.load(f)

    # for item in data:
    #     group = Group(id=item['id'], vk_id=item['vk_id'], name=item['name'], user_status=item['user_status'])
    #     db.session.add(group)

    f = open("app/test_db_data/numbers.json")
    data = json.load(f)

    for item in data:
        number = Number(group_id=item['group_id'], number=item['number'], comment=item['comment'])
        db.session.add(number)

    db.session.commit()
