"""
Models for workout data from Oura API.
"""

from datetime import datetime
from typing import Optional

from peewee import *
from .base import BaseModel


class Workout(BaseModel):
    """
    Model for workout data from Oura API.
    Represents a single workout session tracked by the Oura Ring.
    """

    workout_id = CharField(primary_key=True)
    activity = CharField()
    calories = IntegerField(null=True)
    day = CharField()
    distance = FloatField(null=True)
    start_datetime = DateTimeField()
    end_datetime = DateTimeField()
    intensity = CharField(null=True)
    label = CharField(null=True)
    source = CharField()

    # Optional metrics
    average_heart_rate = IntegerField(null=True)
    max_heart_rate = IntegerField(null=True)
    movement_speed = FloatField(null=True)
    training_energy = IntegerField(null=True)
    training_time = IntegerField(null=True)

    class Meta:
        table_name = "workouts"
