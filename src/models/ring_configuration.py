from peewee import *
from .base import BaseModel

from .personal_info import PersonalInfo


class RingConfiguration(BaseModel):
    """Ring configuration data from Oura API."""

    ring_id = CharField(primary_key=True)
    personal_info = ForeignKeyField(PersonalInfo, backref="ring_configurations")
    color = CharField(null=True)
    design = CharField(null=True)
    firmware_version = CharField(null=True)
    hardware_type = CharField(null=True)
    set_up_at = DateTimeField(null=True)
    size = CharField(null=True)
