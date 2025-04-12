from datetime import datetime

import pytest

from src.models.workout import Workout


def test_create_workout(db_session):
    """Test creating a workout record."""
    workout = Workout(
        workout_id="test123",
        activity="swimming",
        day="2023-12-01",
        start_datetime=datetime(2023, 12, 1, 10, 0),
        end_datetime=datetime(2023, 12, 1, 11, 0),
        source="test",
        distance=1500.0,
        calories=500,
        average_heart_rate=140,
        max_heart_rate=160,
        intensity="medium",
        movement_speed=1.5,
        training_energy=300,
        training_time=3600,
    )

    db_session.add(workout)
    db_session.commit()

    saved_workout = db_session.query(Workout).filter_by(workout_id="test123").first()
    assert saved_workout is not None
    assert saved_workout.activity == "swimming"
    assert saved_workout.distance == 1500.0


def test_workout_required_fields(db_session):
    """Test that required fields must be provided."""
    with pytest.raises(
        Exception
    ):  # SQLAlchemy will raise an error for missing required fields
        workout = Workout(activity="swimming")  # Missing other required fields
        db_session.add(workout)
        db_session.commit()


def test_workout_optional_fields(db_session):
    """Test that optional fields can be null."""
    workout = Workout(
        workout_id="test456",
        activity="swimming",
        day="2023-12-01",
        start_datetime=datetime(2023, 12, 1, 10, 0),
        end_datetime=datetime(2023, 12, 1, 11, 0),
        source="test",
        # Omitting all optional fields
    )

    db_session.add(workout)
    db_session.commit()

    saved_workout = db_session.query(Workout).filter_by(workout_id="test456").first()
    assert saved_workout is not None
    assert saved_workout.calories is None
    assert saved_workout.distance is None
    assert saved_workout.average_heart_rate is None
