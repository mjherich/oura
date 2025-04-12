from .database import db
from .base import BaseModel

# Activity related models
from .activity import ActivitySummary, ActivityContributor
from .daily_activity import DailyActivity
from .workout import Workout

# Sleep related models
from .daily_sleep import DailySleep
from .sleep import (
    SleepPeriod,
    SleepSummary,
    SleepContributor,
    SleepHeartRate,
    SleepHRV,
)

# Health metrics
from .daily_readiness import DailyReadiness
from .spo2 import DailySpO2, SpO2Sample
from .stress import DailyStress, StressSample

# User data
from .personal_info import PersonalInfo

__all__ = [
    # Base
    "BaseModel",
    "db",
    # Activity
    "ActivitySummary",
    "ActivityContributor",
    "DailyActivity",
    "Workout",
    # Sleep
    "DailySleep",
    "SleepPeriod",
    "SleepSummary",
    "SleepContributor",
    "SleepHeartRate",
    "SleepHRV",
    # Health metrics
    "DailyReadiness",
    "DailySpO2",
    "SpO2Sample",
    "DailyStress",
    "StressSample",
    # User data
    "PersonalInfo",
]


def initialize_db():
    """Create the database and tables."""
    MODELS = [
        # Activity
        ActivitySummary,
        ActivityContributor,
        DailyActivity,
        Workout,
        # Sleep
        DailySleep,
        SleepPeriod,
        SleepSummary,
        SleepContributor,
        SleepHeartRate,
        SleepHRV,
        # Health metrics
        DailyReadiness,
        DailySpO2,
        SpO2Sample,
        DailyStress,
        StressSample,
        # User data
        PersonalInfo,
    ]

    with db:
        db.create_tables(MODELS, safe=True)
