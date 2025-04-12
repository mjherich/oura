from peewee import *
from .base import BaseModel


class ReadinessSummary(BaseModel):
    readiness_summary_id = CharField(primary_key=True)
    day = DateField()
    score = IntegerField()
    timestamp = DateTimeField()

    class Meta:
        table_name = "readiness_summaries"


class ReadinessContributor(BaseModel):
    readiness_contributor_id = AutoField()
    readiness_summary = ForeignKeyField(ReadinessSummary, backref="contributors")
    activity_balance = IntegerField()
    body_temperature = IntegerField()
    hrv_balance = IntegerField()
    previous_day_activity = IntegerField()
    previous_night = IntegerField()
    recovery_index = IntegerField()
    resting_heart_rate = IntegerField()
    sleep_balance = IntegerField()

    class Meta:
        table_name = "readiness_contributors"
