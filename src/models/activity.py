from peewee import *
from .base import BaseModel


class ActivitySummary(BaseModel):
    activity_summary_id = CharField(primary_key=True)
    day = DateField()
    score = IntegerField(null=True)
    timestamp = DateTimeField()
    active_calories = IntegerField(null=True)
    total_calories = IntegerField(null=True)
    steps = IntegerField(null=True)
    equivalent_walking_distance = IntegerField(null=True)
    inactivity_alerts = IntegerField(null=True)
    non_wear_time = IntegerField(null=True)
    resting_time = IntegerField(null=True)
    meters_to_target = IntegerField(null=True)
    target_calories = IntegerField(null=True)
    target_meters = IntegerField(null=True)
    sedentary_time = IntegerField(null=True)

    class Meta:
        table_name = "activity_summaries"


class ActivityContributor(BaseModel):
    activity_contributor_id = AutoField()
    activity_summary = ForeignKeyField(ActivitySummary, backref="contributors")
    meet_daily_targets = IntegerField(null=True)
    move_every_hour = IntegerField(null=True)
    recovery_time = IntegerField(null=True)
    stay_active = IntegerField(null=True)
    training_frequency = IntegerField(null=True)
    training_volume = IntegerField(null=True)

    class Meta:
        table_name = "activity_contributors"
