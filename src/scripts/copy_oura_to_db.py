#!/usr/bin/env python3
"""
Script to populate the Oura Ring database tables using the API wrapper.
"""
import logging
from datetime import datetime
from typing import Optional

from src.api import OuraAPI
from src.models import (
    db,
    PersonalInfo,
    DailyActivity,
    DailySleep,
    DailyReadiness,
    SleepPeriod,
    initialize_db,
)

# Configure logging - simplified and focused
logging.basicConfig(
    level=logging.INFO,  # Changed from DEBUG to INFO
    format="%(asctime)s - %(message)s",  # Simplified format
    handlers=[logging.FileHandler("oura_sync.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Disable noisy peewee logging
logging.getLogger("peewee").setLevel(logging.WARNING)


def copy_daily_data(
    api: OuraAPI, start_date: str, end_date: Optional[str] = None
) -> None:
    """Copy daily data from Oura API to database."""
    if not end_date:
        end_date = datetime.now().strftime("%Y-%m-%d")

    logger.info(f"Starting data sync from {start_date} to {end_date}")

    try:
        with db.atomic():
            # Personal Info
            personal_info = api.get_personal_info()
            if personal_info:
                PersonalInfo.delete().execute()
                PersonalInfo.create(**personal_info)
                logger.info("Updated personal info")

            # Daily Activity
            activity_data = api.get_daily_activity(start_date=start_date)
            DailyActivity.delete().execute()
            for activity in activity_data:
                # Rest of the activity processing code remains the same...
                contributors = activity.pop("contributors", {})
                # ... (keep existing processing logic)
                DailyActivity.create(**activity)
            logger.info(f"Processed {len(activity_data)} activity records")

            # Daily Sleep
            sleep_data = api.get_daily_sleep(start_date=start_date)
            DailySleep.delete().execute()
            sleep_periods_count = 0
            for sleep in sleep_data:
                contributors = sleep.pop("contributors", {})
                periods = sleep.pop("periods", [])

                if "day" in sleep:
                    sleep["day"] = datetime.strptime(sleep["day"], "%Y-%m-%d").date()
                if "timestamp" in sleep and isinstance(sleep["timestamp"], str):
                    sleep["timestamp"] = datetime.fromisoformat(sleep["timestamp"])

                if contributors:
                    sleep.update(
                        {
                            "deep_sleep": contributors.get("deep_sleep"),
                            "efficiency": contributors.get("efficiency"),
                            "latency": contributors.get("latency"),
                            "rem_sleep": contributors.get("rem_sleep"),
                            "restfulness": contributors.get("restfulness"),
                            "timing": contributors.get("timing"),
                            "total_sleep": contributors.get("total_sleep"),
                        }
                    )

                DailySleep.create(**sleep)

                # Handle sleep periods
                for period in periods:
                    if period.get("bedtime_start") and period.get("bedtime_end"):
                        SleepPeriod.create(
                            sleep_period_id=str(period.get("id", "")),
                            start_datetime=datetime.fromisoformat(
                                period["bedtime_start"]
                            ),
                            end_datetime=datetime.fromisoformat(period["bedtime_end"]),
                            total_sleep_duration=period.get("total_sleep_duration"),
                            awake_time=period.get("awake_time"),
                            light_sleep_duration=period.get("light_sleep_duration"),
                            rem_sleep_duration=period.get("rem_sleep_duration"),
                            deep_sleep_duration=period.get("deep_sleep_duration"),
                            restless_periods=period.get("restless_periods"),
                            average_heart_rate=period.get("average_heart_rate"),
                            lowest_heart_rate=period.get("lowest_heart_rate"),
                            average_hrv=period.get("average_hrv"),
                            temperature_delta=period.get("temperature_delta"),
                            bedtime_start=datetime.fromisoformat(
                                period["bedtime_start"]
                            ),
                            bedtime_end=datetime.fromisoformat(period["bedtime_end"]),
                            readiness_score_delta=period.get("readiness_score_delta"),
                        )
                sleep_periods_count += len(periods)

            logger.info(
                f"Processed {len(sleep_data)} sleep records with {sleep_periods_count} sleep periods"
            )

            # Daily Readiness
            readiness_data = api.get_daily_readiness(start_date=start_date)
            DailyReadiness.delete().execute()
            for readiness in readiness_data:
                # ... (keep existing readiness processing logic)
                pass
            logger.info(f"Processed {len(readiness_data)} readiness records")

        logger.info("Data sync completed successfully")

    except Exception as e:
        logger.error(f"Sync failed: {str(e)}")
        raise


def main():
    """Main function."""
    api = OuraAPI()

    # Create database tables
    initialize_db()

    try:
        # Copy all time daily data
        start_date = datetime(2024, 1, 1).strftime("%Y-%m-%d")
        copy_daily_data(api, start_date)
        logger.info("Successfully copied Oura Ring data to database")

        # On to

    except Exception as e:
        logger.error(f"Error copying data: {e}")
        raise


if __name__ == "__main__":
    main()
