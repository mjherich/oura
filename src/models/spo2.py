"""
Models for SpO2 (blood oxygen saturation) data from Oura API.
"""

from peewee import *
from .base import BaseModel


class DailySpO2(BaseModel):
    """Model for daily SpO2 data."""

    daily_spo2_id = CharField(primary_key=True)
    day = CharField()
    timestamp = DateTimeField()
    average = FloatField(null=True)
    breathing_disturbance_index = IntegerField(null=True)

    class Meta:
        table_name = "daily_spo2"


class SpO2Sample(BaseModel):
    """Model for individual SpO2 measurements."""

    spo2_sample_id = CharField(primary_key=True)
    daily_spo2 = ForeignKeyField(DailySpO2, backref="samples")
    timestamp = DateTimeField()
    value = FloatField()

    class Meta:
        table_name = "spo2_samples"
