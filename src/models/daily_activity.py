from peewee import *
from .base import BaseModel


class DailyActivity(BaseModel):
    """Daily activity data from Oura API."""

    daily_activity_id = AutoField()
    activity_summary_id = CharField(unique=True)
    day = DateField(index=True)
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
    # Contributors
    meet_daily_targets = IntegerField(null=True)
    move_every_hour = IntegerField(null=True)
    recovery_time = IntegerField(null=True)
    stay_active = IntegerField(null=True)
    training_frequency = IntegerField(null=True)
    training_volume = IntegerField(null=True)

    class Meta:
        table_name = "daily_activities"
