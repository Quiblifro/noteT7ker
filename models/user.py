from peewee import *
from datetime import datetime
from .base_model import BaseModel, dbhandle

class User(BaseModel):
    id = PrimaryKeyField(null=False)
    telegram_id = IntegerField()
    name = CharField(max_length=150)
 
    created_at = DateTimeField(default = datetime.now)
    updated_at = DateTimeField(default = datetime.now)

    class Meta:
        db_table = "users"
        order_by = ('created_at',)

if __name__ == '__main__':
    try:
        dbhandle.connect()
        User.create_table()
    except InternalError as px:
        print(str(px))