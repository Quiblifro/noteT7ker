from peewee import *
from datetime import datetime
from .base_model import BaseModel, dbhandle
from .user import User

class Note(BaseModel):
    id = PrimaryKeyField(null=False)
    content = TextField()
    author = ForeignKeyField(User, to_field='id', on_delete='cascade', on_update='cascade')

    created_at = DateTimeField(default = datetime.now)
    updated_at = DateTimeField(default = datetime.now)

    class Meta:
        db_table = "notes"
        order_by = ('created_at',)

if __name__ == '__main__':
    try:
        dbhandle.connect()
        Note.create_table()
    except InternalError as px:
        print(str(px))