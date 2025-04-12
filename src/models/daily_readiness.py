from peewee import *
from .base import BaseModel


class DailyReadiness(BaseModel):
    """Daily readiness data from Oura API."""

    readiness_summary_id = CharField(primary_key=True)
    day = DateField(index=True)
    score = IntegerField(null=True)
    timestamp = DateTimeField()
    # Contributors
    activity_balance = IntegerField(null=True)
    body_temperature = IntegerField(null=True)
    hrv_balance = IntegerField(null=True)
    previous_day_activity = IntegerField(null=True)
    previous_night = IntegerField(null=True)
    recovery_index = IntegerField(null=True)
    resting_heart_rate = IntegerField(null=True)
    sleep_balance = IntegerField(null=True)

    class Meta:
        table_name = "daily_readiness"
