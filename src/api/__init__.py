"""
Oura Ring API wrapper that loads API key from .env file.
"""

import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple, TypedDict, Union

import requests
from dotenv import load_dotenv
from oura_ring import OuraClient

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("oura_sync.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class PersonalInfoDict(TypedDict):
    """Type definition for personal info response."""

    personal_info_id: str
    age: Optional[int]
    weight: Optional[float]
    height: Optional[float]
    biological_sex: Optional[str]
    email: Optional[str]


class SleepContributorDict(TypedDict):
    """Type definition for sleep contributor response."""

    deep_sleep: Optional[int]
    efficiency: Optional[int]
    latency: Optional[int]
    rem_sleep: Optional[int]
    restfulness: Optional[int]
    timing: Optional[int]
    total_sleep: Optional[int]


class SleepPeriodDict(TypedDict):
    """Type definition for sleep period response."""

    sleep_period_id: str
    start_datetime: datetime
    end_datetime: datetime
    total_sleep_duration: Optional[int]
    awake_time: Optional[int]
    light_sleep_duration: Optional[int]
    rem_sleep_duration: Optional[int]
    deep_sleep_duration: Optional[int]
    restless_periods: Optional[int]
    average_heart_rate: Optional[int]
    lowest_heart_rate: Optional[int]
    average_hrv: Optional[int]
    temperature_delta: Optional[float]
    bedtime_start: Optional[datetime]
    bedtime_end: Optional[datetime]
    readiness_score_delta: Optional[int]


class SleepSummaryDict(TypedDict):
    """Type definition for sleep summary response."""

    sleep_summary_id: str
    day: str
    score: Optional[int]
    timestamp: datetime
    contributors: Optional[SleepContributorDict]
    periods: List[SleepPeriodDict]


class ActivityContributorDict(TypedDict):
    """Type definition for activity contributor response."""

    meet_daily_targets: Optional[int]
    move_every_hour: Optional[int]
    recovery_time: Optional[int]
    stay_active: Optional[int]
    training_frequency: Optional[int]
    training_volume: Optional[int]


class ActivitySummaryDict(TypedDict):
    """Type definition for activity summary response."""

    activity_summary_id: str
    day: str
    score: Optional[int]
    timestamp: datetime
    active_calories: Optional[int]
    total_calories: Optional[int]
    steps: Optional[int]
    equivalent_walking_distance: Optional[int]
    inactivity_alerts: Optional[int]
    non_wear_time: Optional[int]
    resting_time: Optional[int]
    meters_to_target: Optional[int]
    target_calories: Optional[int]
    target_meters: Optional[int]
    sedentary_time: Optional[int]
    contributors: Optional[ActivityContributorDict]


class ReadinessContributorDict(TypedDict):
    """Type definition for readiness contributor response."""

    activity_balance: Optional[int]
    body_temperature: Optional[int]
    hrv_balance: Optional[int]
    previous_day_activity: Optional[int]
    previous_night: Optional[int]
    recovery_index: Optional[int]
    resting_heart_rate: Optional[int]
    sleep_balance: Optional[int]


class ReadinessSummaryDict(TypedDict):
    """Type definition for readiness summary response."""

    readiness_summary_id: str
    day: str
    score: Optional[int]
    timestamp: datetime
    contributors: Optional[ReadinessContributorDict]


class HeartRateDict(TypedDict):
    """Type definition for heart rate response."""

    sleep_hr_id: int
    timestamp: datetime
    bpm: Optional[int]


class HRVDict(TypedDict):
    """Type definition for HRV response."""

    sleep_hrv_id: int
    timestamp: datetime
    rmssd: Optional[int]


class WorkoutDict(TypedDict):
    """Type definition for workout response."""

    workout_id: str
    activity: str
    calories: Optional[int]
    day: str
    distance: Optional[float]
    start_datetime: datetime
    end_datetime: datetime
    intensity: Optional[str]
    label: Optional[str]
    source: str
    average_heart_rate: Optional[int]
    max_heart_rate: Optional[int]
    movement_speed: Optional[float]
    training_energy: Optional[int]
    training_time: Optional[int]


class DailySpO2Dict(TypedDict):
    """Type definition for daily SpO2 response."""

    daily_spo2_id: str
    day: str
    timestamp: datetime
    average: Optional[float]
    breathing_disturbance_index: Optional[int]


class DailyStressDict(TypedDict):
    """Type definition for daily stress response."""

    daily_stress_id: str
    day: str
    timestamp: datetime
    stress_high: Optional[int]
    recovery_high: Optional[int]
    day_summary: Optional[str]


class SpO2SampleDict(TypedDict):
    """Type definition for SpO2 sample response."""

    spo2_sample_id: str
    daily_spo2_id: str
    timestamp: datetime
    value: float


class StressSampleDict(TypedDict):
    """Type definition for stress sample response."""

    stress_sample_id: str
    daily_stress_id: str
    timestamp: datetime
    value: Optional[int]
    source: str


class OuraAPI:
    """Wrapper for the Oura Ring API."""

    def __init__(self):
        """Initialize the API client."""
        logger.info("Initializing OuraAPI")
        load_dotenv()

        self.api_token = os.getenv("OURA_API_TOKEN")
        if not self.api_token:
            logger.error("OURA_API_TOKEN not found in environment variables")
            raise ValueError("OURA_API_TOKEN not found in environment variables")

        logger.info("Creating Oura client")
        self.client = OuraClient(self.api_token)
        logger.debug("OuraAPI initialized successfully")

    def get_personal_info(self) -> PersonalInfoDict:
        """Get personal information from the API."""
        logger.info("Fetching personal information")
        try:
            response = self.client.get_personal_info()
            logger.debug(f"Personal info response: {response}")

            if not response:
                logger.error("Empty response from personal_info API call")
                return None

            return {
                "personal_info_id": response.get("id", ""),
                "age": response.get("age"),
                "weight": response.get("weight"),
                "height": response.get("height"),
                "biological_sex": response.get("biological_sex"),
                "email": response.get("email"),
            }
        except Exception as e:
            logger.error(f"Error fetching personal info: {str(e)}", exc_info=True)
            raise

    def get_daily_sleep(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[SleepSummaryDict]:
        """Get daily sleep data with periods and contributors."""
        sleep_data = self.client.get_daily_sleep(
            start_date=start_date, end_date=end_date
        )
        return [
            {
                "sleep_summary_id": str(sleep.get("id", "")),
                "day": sleep.get("day"),
                "score": sleep.get("score"),
                "timestamp": (
                    datetime.fromisoformat(sleep["timestamp"])
                    if sleep.get("timestamp")
                    else None
                ),
                "contributors": sleep.get("contributors"),
                "periods": sleep.get("sleep_periods", []),
            }
            for sleep in sleep_data
        ]

    def get_daily_activity(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[ActivitySummaryDict]:
        """Get daily activity data with contributors."""
        activity_data = self.client.get_daily_activity(
            start_date=start_date, end_date=end_date
        )
        return [
            {
                "activity_summary_id": str(activity.get("id", "")),
                "day": activity.get("day"),
                "score": activity.get("score"),
                "timestamp": (
                    datetime.fromisoformat(activity["timestamp"])
                    if activity.get("timestamp")
                    else None
                ),
                "active_calories": activity.get("active_calories"),
                "total_calories": activity.get("total_calories"),
                "steps": activity.get("steps"),
                "equivalent_walking_distance": activity.get(
                    "equivalent_walking_distance"
                ),
                "inactivity_alerts": activity.get("inactivity_alerts"),
                "non_wear_time": activity.get("non_wear_time"),
                "resting_time": activity.get("resting_time"),
                "meters_to_target": activity.get("meters_to_target"),
                "target_calories": activity.get("target_calories"),
                "target_meters": activity.get("target_meters"),
                "sedentary_time": activity.get("sedentary_time"),
                "contributors": activity.get("contributors"),
            }
            for activity in activity_data
        ]

    def get_daily_readiness(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[ReadinessSummaryDict]:
        """Get daily readiness data with contributors."""
        readiness_data = self.client.get_daily_readiness(
            start_date=start_date, end_date=end_date
        )
        return [
            {
                "readiness_summary_id": str(readiness.get("id", "")),
                "day": readiness.get("day"),
                "score": readiness.get("score"),
                "timestamp": (
                    datetime.fromisoformat(readiness["timestamp"])
                    if readiness.get("timestamp")
                    else None
                ),
                "contributors": readiness.get("contributors"),
            }
            for readiness in readiness_data
        ]

    def get_heart_rate(
        self, start_date_time: str, end_date_time: str
    ) -> List[HeartRateDict]:
        """Get heart rate data."""
        hr_data = self.client.get_heart_rate(start_date_time, end_date_time)
        return [
            {
                "sleep_hr_id": i,  # Auto-incrementing ID will be handled by SQLAlchemy
                "timestamp": (
                    datetime.fromisoformat(hr["timestamp"])
                    if hr.get("timestamp")
                    else None
                ),
                "bpm": hr.get("bpm"),
            }
            for i, hr in enumerate(hr_data)
        ]

    def get_hrv(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[HRVDict]:
        """Get HRV data."""
        hrv_data = self.client.get_heart_rate(
            start_date=start_date, end_date=end_date
        )  # Using heart_rate endpoint as example
        return [
            {
                "sleep_hrv_id": i,  # Auto-incrementing ID will be handled by SQLAlchemy
                "timestamp": (
                    datetime.fromisoformat(hrv["timestamp"])
                    if hrv.get("timestamp")
                    else None
                ),
                "rmssd": hrv.get(
                    "hrv"
                ),  # Assuming HRV data is available in the response
            }
            for i, hrv in enumerate(hrv_data)
        ]

    def get_workouts(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[WorkoutDict]:
        """Get workout data from Oura API.

        Args:
            start_date: Start date in YYYY-MM-DD format. Defaults to yesterday.
            end_date: End date in YYYY-MM-DD format. Defaults to today.

        Returns:
            List of workout data dictionaries.
        """
        logger.info("Fetching workout data")
        try:
            if not start_date:
                start_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            if not end_date:
                end_date = datetime.now().strftime("%Y-%m-%d")

            workouts = self.client.get_workouts(
                start_date=start_date, end_date=end_date
            )

            return [
                {
                    "workout_id": workout["id"],
                    "activity": workout["activity"],
                    "calories": workout.get("calories"),
                    "day": workout["day"],
                    "distance": workout.get("distance"),
                    "start_datetime": datetime.fromisoformat(workout["start_datetime"]),
                    "end_datetime": datetime.fromisoformat(workout["end_datetime"]),
                    "intensity": workout.get("intensity"),
                    "label": workout.get("label"),
                    "source": workout["source"],
                    "average_heart_rate": workout.get("heart_rate", {}).get("average"),
                    "max_heart_rate": workout.get("heart_rate", {}).get("max"),
                    "movement_speed": workout.get("movement_speed", {}).get("average"),
                    "training_energy": workout.get("training_energy"),
                    "training_time": workout.get("training_time"),
                }
                for workout in workouts
            ]
        except Exception as e:
            logger.error(f"Error fetching workout data: {str(e)}", exc_info=True)
            raise

    def get_daily_spo2(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[DailySpO2Dict]:
        """Get daily SpO2 data from Oura API.

        Args:
            start_date: Start date in YYYY-MM-DD format. Defaults to yesterday.
            end_date: End date in YYYY-MM-DD format. Defaults to today.

        Returns:
            List of daily SpO2 data.
        """
        logger.info("Fetching daily SpO2 data")
        try:
            if not start_date:
                start_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            if not end_date:
                end_date = datetime.now().strftime("%Y-%m-%d")

            spo2_data = self.client.get_daily_spo2(
                start_date=start_date, end_date=end_date
            )

            results = []
            seen_days = set()  # To handle duplicate days
            print(f"Total days: {len(spo2_data)}")
            for daily_data in spo2_data:
                if not daily_data:  # Skip if no data
                    continue

                day = daily_data.get("day")
                if not day or day in seen_days:
                    continue
                seen_days.add(day)

                daily_dict: DailySpO2Dict = {
                    "daily_spo2_id": daily_data.get("id", ""),
                    "day": day,
                    "timestamp": datetime.fromisoformat(day + "T00:00:00+00:00"),
                    "average": (
                        daily_data.get("spo2_percentage", {}).get("average")
                        if daily_data.get("spo2_percentage")
                        else None
                    ),
                    "breathing_disturbance_index": daily_data.get(
                        "breathing_disturbance_index"
                    ),
                }
                results.append(daily_dict)

            return results
        except Exception as e:
            logger.error(f"Error fetching daily SpO2 data: {str(e)}", exc_info=True)
            raise

    def get_daily_stress(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[DailyStressDict]:
        """Get daily stress data from Oura API.

        Args:
            start_date: Start date in YYYY-MM-DD format. Defaults to yesterday.
            end_date: End date in YYYY-MM-DD format. Defaults to today.

        Returns:
            List of daily stress data.
        """
        logger.info("Fetching daily stress data")
        try:
            if not start_date:
                start_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            if not end_date:
                end_date = datetime.now().strftime("%Y-%m-%d")

            stress_data = self.client.get_daily_stress(
                start_date=start_date, end_date=end_date
            )

            results = []

            for daily_data in stress_data:
                if not daily_data:  # Skip if no data
                    continue

                daily_dict: DailyStressDict = {
                    "daily_stress_id": daily_data.get("id", ""),
                    "day": daily_data.get("day"),
                    "timestamp": datetime.fromisoformat(
                        daily_data["day"] + "T00:00:00+00:00"
                    ),
                    "stress_high": daily_data.get("stress_high"),
                    "recovery_high": daily_data.get("recovery_high"),
                    "day_summary": daily_data.get("day_summary"),
                }
                results.append(daily_dict)

            return results
        except Exception as e:
            logger.error(f"Error fetching daily stress data: {str(e)}", exc_info=True)
            raise

    def get_sleep_heart_rate(
        self,
        start_datetime: Optional[datetime] = None,
        end_datetime: Optional[datetime] = None,
    ) -> List[HeartRateDict]:
        """Get sleep heart rate data.

        Args:
            start_datetime: Start datetime in UTC. Expected in ISO 8601 format (YYYY-MM-DDThh:mm:ss).
            end_datetime: End datetime in UTC. Expected in ISO 8601 format (YYYY-MM-DDThh:mm:ss).
        """
        logger.info("Fetching sleep heart rate data")
        try:
            if not start_datetime:
                start_datetime = datetime.now(timezone.utc) - timedelta(days=1)
            if not end_datetime:
                end_datetime = datetime.now(timezone.utc)

            # Format datetimes in ISO 8601 format exactly as specified in docs
            start_str = start_datetime.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            end_str = end_datetime.strftime("%Y-%m-%dT%H:%M:%S.000Z")

            hr_data = self.client.get_heart_rate(
                start_datetime=start_str, end_datetime=end_str
            )

            return [
                {
                    "sleep_hr_id": i,
                    "timestamp": datetime.fromisoformat(hr["timestamp"]),
                    "bpm": hr.get("bpm"),
                }
                for i, hr in enumerate(hr_data)
                if hr.get("source") == "sleep" and hr.get("timestamp")
            ]
        except Exception as e:
            logger.error(f"Error fetching sleep heart rate: {str(e)}", exc_info=True)
            return []  # Return empty list instead of raising

    def get_ring_configuration(self) -> List[Dict[str, Any]]:
        """Get ring configuration data."""
        logger.info("Fetching ring configuration")
        try:
            config_data = self.client.get_ring_configuration()

            return [
                {
                    "ring_id": config.get("id", ""),
                    "color": config.get("color"),
                    "design": config.get("design"),
                    "firmware_version": config.get("firmware_version"),
                    "hardware_type": config.get("hardware_type"),
                    "set_up_at": (
                        datetime.fromisoformat(config["set_up_at"])
                        if config.get("set_up_at")
                        else None
                    ),
                    "size": config.get("size"),
                }
                for config in config_data
            ]
        except Exception as e:
            logger.error(f"Error fetching ring configuration: {str(e)}", exc_info=True)
            return []  # Return empty list instead of raising

    def get_spo2_samples(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[SpO2SampleDict]:
        """Get SpO2 sample data."""
        logger.info("Fetching SpO2 samples")
        try:
            daily_spo2 = self.get_daily_spo2(start_date=start_date, end_date=end_date)
            samples = []

            for daily in daily_spo2:
                if daily.get("samples"):
                    for sample in daily["samples"]:
                        sample_dict: SpO2SampleDict = {
                            "spo2_sample_id": sample.get("id", ""),
                            "daily_spo2_id": daily["daily_spo2_id"],
                            "timestamp": datetime.fromisoformat(sample["timestamp"]),
                            "value": sample.get("value", 0.0),
                        }
                        samples.append(sample_dict)

            return samples
        except Exception as e:
            logger.error(f"Error fetching SpO2 samples: {str(e)}", exc_info=True)
            raise

    def get_stress_samples(
        self, start_date: Optional[str] = None, end_date: Optional[str] = None
    ) -> List[StressSampleDict]:
        """Get stress sample data."""
        logger.info("Fetching stress samples")
        try:
            daily_stress = self.get_daily_stress(
                start_date=start_date, end_date=end_date
            )
            samples = []

            for daily in daily_stress:
                if daily.get("samples"):
                    for sample in daily["samples"]:
                        sample_dict: StressSampleDict = {
                            "stress_sample_id": sample.get("id", ""),
                            "daily_stress_id": daily["daily_stress_id"],
                            "timestamp": datetime.fromisoformat(sample["timestamp"]),
                            "value": sample.get("value"),
                            "source": sample.get("source", ""),
                        }
                        samples.append(sample_dict)

            return samples
        except Exception as e:
            logger.error(f"Error fetching stress samples: {str(e)}", exc_info=True)
            raise
