"""
Models for stress data from Oura API.
"""

from datetime import datetime
from typing import Optional

from peewee import *
from src.models.base import BaseModel


class DailyStress(BaseModel):
    """Model for daily stress data."""

    daily_stress_id = CharField(primary_key=True)
    day = DateField()
    timestamp = DateTimeField()
    stress_high = IntegerField(null=True)
    recovery_high = IntegerField(null=True)
    day_summary = CharField(null=True)

    def __repr__(self):
        return f"<DailyStress(id={self.daily_stress_id}, day={self.day}, stress_high={self.stress_high})>"

    class Meta:
        table_name = "daily_stress"


class StressSample(BaseModel):
    """Model for individual stress measurements."""

    stress_sample_id = CharField(primary_key=True)
    daily_stress = ForeignKeyField(DailyStress, backref="samples")
    timestamp = DateTimeField()
    value = FloatField()
    source = CharField()

    class Meta:
        table_name = "stress_samples"
