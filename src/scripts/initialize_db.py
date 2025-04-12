#!/usr/bin/env python

from src.models.activity import ActivitySummary, ActivityContributor
from src.models.daily_activity import DailyActivity
from src.models.daily_sleep import DailySleep
from src.models.readiness import ReadinessSummary, ReadinessContributor
from src.models.personal_info import PersonalInfo
from src.models.database import db

MODELS = [
    ActivitySummary,
    ActivityContributor,
    DailyActivity,
    DailySleep,
    ReadinessSummary,
    ReadinessContributor,
    PersonalInfo,
]


def initialize_db():
    """Initialize the database and create tables."""
    db.connect()

    # This will create tables with the correct names from Meta classes
    db.create_tables(MODELS, safe=True)

    db.close()


if __name__ == "__main__":
    initialize_db()
