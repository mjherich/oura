from peewee import Model
from .database import db  # Make sure this points to your database instance


class BaseModel(Model):
    class Meta:
        database = db
