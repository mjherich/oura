from peewee import *
from .base import BaseModel


class SleepSummary(BaseModel):
    sleep_summary_id = CharField(primary_key=True)
    day = DateField()
    score = IntegerField(null=True)
    timestamp = DateTimeField()

    class Meta:
        table_name = "sleep_summaries"


class SleepContributor(BaseModel):
    sleep_contributor_id = AutoField()
    sleep_summary = ForeignKeyField(SleepSummary, backref="contributors")
    deep_sleep = IntegerField(null=True)
    efficiency = IntegerField(null=True)
    latency = IntegerField(null=True)
    rem_sleep = IntegerField(null=True)
    restfulness = IntegerField(null=True)
    timing = IntegerField(null=True)
    total_sleep = IntegerField(null=True)

    class Meta:
        table_name = "sleep_contributors"


class SleepPeriod(BaseModel):
    sleep_period_id = CharField(primary_key=True)
    sleep_summary = ForeignKeyField(SleepSummary, backref="periods")
    start_datetime = DateTimeField()
    end_datetime = DateTimeField()
    total_sleep_duration = IntegerField(null=True)  # in seconds
    awake_time = IntegerField(null=True)  # in seconds
    light_sleep_duration = IntegerField(null=True)  # in seconds
    rem_sleep_duration = IntegerField(null=True)  # in seconds
    deep_sleep_duration = IntegerField(null=True)  # in seconds
    restless_periods = IntegerField(null=True)
    average_heart_rate = IntegerField(null=True)
    lowest_heart_rate = IntegerField(null=True)
    average_hrv = IntegerField(null=True)
    temperature_delta = FloatField(null=True)
    bedtime_start = DateTimeField(null=True)
    bedtime_end = DateTimeField(null=True)
    readiness_score_delta = IntegerField(null=True)

    class Meta:
        table_name = "sleep_periods"


class SleepHeartRate(BaseModel):
    sleep_hr_id = AutoField()
    sleep_period = ForeignKeyField(SleepPeriod, backref="heart_rate_data")
    timestamp = DateTimeField()
    bpm = IntegerField(null=True)

    class Meta:
        table_name = "sleep_heart_rates"


class SleepHRV(BaseModel):
    sleep_hrv_id = AutoField()
    sleep_period = ForeignKeyField(SleepPeriod, backref="hrv_data")
    timestamp = DateTimeField()
    rmssd = IntegerField(null=True)

    class Meta:
        table_name = "sleep_hrvs"
