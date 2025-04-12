from peewee import *
from .base import BaseModel


class DailySleep(BaseModel):
    """Daily sleep data from Oura API."""

    daily_sleep_id = AutoField()
    sleep_summary_id = CharField()
    day = DateField(index=True)
    score = IntegerField(null=True)
    timestamp = DateTimeField()
    # Contributors
    deep_sleep = IntegerField(null=True)
    efficiency = IntegerField(null=True)
    latency = IntegerField(null=True)
    rem_sleep = IntegerField(null=True)
    restfulness = IntegerField(null=True)
    timing = IntegerField(null=True)
    total_sleep = IntegerField(null=True)

    class Meta:
        table_name = "daily_sleep"
