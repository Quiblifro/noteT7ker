from peewee import MySQLDatabase, Model

import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')

dbhandle = MySQLDatabase(
    DB_NAME, 
    user = DB_USER,
    password = DB_PASS,
    host = DB_HOST
)

class BaseModel(Model):
    class Meta:
        database = dbhandle