from peewee import *
from .base import BaseModel


class PersonalInfo(BaseModel):
    """Personal information from Oura API."""

    personal_info_id = CharField(primary_key=True)
    age = IntegerField(null=True)
    weight = FloatField(null=True)
    height = FloatField(null=True)
    biological_sex = CharField(null=True)
    email = CharField(null=True)

    class Meta:
        table_name = "personal_info"
