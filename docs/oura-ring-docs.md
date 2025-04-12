Title: GitHub - hedgertronic/oura-ring: Tools for acquiring and analyzing Oura API data.

URL Source: https://github.com/hedgertronic/oura-ring

Markdown Content:
Oura Ring for Python
--------------------

[](https://github.com/hedgertronic/oura-ring#oura-ring-for-python-)

Tools for acquiring and analyzing Oura API data.

[Oura](https://ouraring.com/) is a wearable ring for monitoring sleep, activity, and workouts.

Contents
--------

[](https://github.com/hedgertronic/oura-ring#contents-)

*   [Installation](https://github.com/hedgertronic/oura-ring#installation)
*   [Getting Started](https://github.com/hedgertronic/oura-ring#getting-started)
*   [API Requests](https://github.com/hedgertronic/oura-ring#api-requests)
    *   [Get Personal Info](https://github.com/hedgertronic/oura-ring#get-personal-info)
    *   [Get Daily Sleep](https://github.com/hedgertronic/oura-ring#get-daily-sleep)
    *   [Get Daily SpO2](https://github.com/hedgertronic/oura-ring#get-daily-spo2)
    *   [Get Daily Stress](https://github.com/hedgertronic/oura-ring#get-daily-stress)
    *   [Get Daily Activity](https://github.com/hedgertronic/oura-ring#get-daily-activity)
    *   [Get Daily Readiness](https://github.com/hedgertronic/oura-ring#get-daily-readiness)
    *   [Get Enhanced Tag](https://github.com/hedgertronic/oura-ring#get-enhanced-tag)
    *   [Get Heart Rate](https://github.com/hedgertronic/oura-ring#get-heart-rate)
    *   [Get Ring Configuration](https://github.com/hedgertronic/oura-ring#get-ring-configuration)
    *   [Get Rest Mode Period](https://github.com/hedgertronic/oura-ring#get-rest-mode-period)
    *   [Get Sleep Periods](https://github.com/hedgertronic/oura-ring#get-sleep-periods)
    *   [Get Sleep Time](https://github.com/hedgertronic/oura-ring#get-sleep-time)
    *   [Get Sessions](https://github.com/hedgertronic/oura-ring#get-sessions)
    *   [Get Tags](https://github.com/hedgertronic/oura-ring#get-tags)
    *   [Get Workouts](https://github.com/hedgertronic/oura-ring#get-workouts)
*   [Usage With DataFrame](https://github.com/hedgertronic/oura-ring#usage-with-dataframe)

Installation
------------

[](https://github.com/hedgertronic/oura-ring#installation)

The `oura_ring` module can be installed via pip:

`pip install oura-ring`

Getting Started
---------------

[](https://github.com/hedgertronic/oura-ring#getting-started)

In order to use the Oura client, you must first generate a [`personal_access_token`](https://cloud.ouraring.com/personal-access-tokens) for your Oura account.

It is best practice to store this value in a `.env` file:

# Oura credentials
PERSONAL\_ACCESS\_TOKEN="<PERSONAL\_ACCESS\_TOKEN\>"

You can use [`python-dotenv`](https://github.com/theskumar/python-dotenv) to load the enviroment variables for use in code:

import os
from dotenv import load\_dotenv

load\_dotenv()

pat \= os.getenv("PERSONAL\_ACCESS\_TOKEN") or ""

Once the environment variables are loaded, an `OuraClient` object can be created:

from oura\_ring import OuraClient

\# Using a traditional constructor
client \= OuraClient(pat)
...

\# Using a context manager
with OuraClient(pat) as client:
    ...

API Requests
------------

[](https://github.com/hedgertronic/oura-ring#api-requests)

There are nine different API requests that `OuraClient` can make. Full Oura API v2 documentation can be found on [Oura's website](https://cloud.ouraring.com/v2/docs).

### Get Personal Info

[](https://github.com/hedgertronic/oura-ring#get-personal-info)

**Method**: `get_personal_info()`

**Payload**: None

**Example Response**:

{
    "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
    "age": 31,
    "weight": 74.8,
    "height": 1.8,
    "biological\_sex": "male",
    "email": "example@example.com"
}

### Get Daily Sleep

[](https://github.com/hedgertronic/oura-ring#get-daily-sleep)

**Method**: `get_daily_sleep(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "contributors": {
            "deep\_sleep": 57,
            "efficiency": 98,
            "latency": 81,
            "rem\_sleep": 20,
            "restfulness": 54,
            "timing": 84,
            "total\_sleep": 60
        },
        "day": "2022-07-14",
        "score": 63,
        "timestamp": "2022-07-14T00:00:00+00:00"
    },
    ...
\]

### Get Daily Activity

[](https://github.com/hedgertronic/oura-ring#get-daily-activity)

**Method**: `get_daily_activity(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "class\_5\_min": "<long sequence of 0|1|2|3|4|5\>",
        "score": 82,
        "active\_calories": 1222,
        "average\_met\_minutes": 1.90625,
        "contributors": {
            "meet\_daily\_targets": 43,
            "move\_every\_hour": 100,
            "recovery\_time": 100,
            "stay\_active": 98,
            "training\_frequency": 71,
            "training\_volume": 98
        },
        "equivalent\_walking\_distance": 20122,
        "high\_activity\_met\_minutes": 444,
        "high\_activity\_time": 3000,
        "inactivity\_alerts": 0,
        "low\_activity\_met\_minutes": 117,
        "low\_activity\_time": 10020,
        "medium\_activity\_met\_minutes": 391,
        "medium\_activity\_time": 6060,
        "met": {
            "interval": 60,
            "items": \[
                0.1,
                ...
            \],
            "timestamp": "2021-11-26T04:00:00.000-08:00"
        },
        "meters\_to\_target": \-16200,
        "non\_wear\_time": 27480,
        "resting\_time": 18840,
        "sedentary\_met\_minutes": 10,
        "sedentary\_time": 21000,
        "steps": 18430,
        "target\_calories": 350,
        "target\_meters": 7000,
        "total\_calories": 3446,
        "day": "2021-11-26",
        "timestamp": "2021-11-26T04:00:00-08:00"
    },
    ...
\]

### Get Daily Readiness

[](https://github.com/hedgertronic/oura-ring#get-daily-readiness)

**Method**: `get_daily_readiness(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "contributors": {
            "activity\_balance": 56,
            "body\_temperature": 98,
            "hrv\_balance": 75,
            "previous\_day\_activity": None,
            "previous\_night": 35,
            "recovery\_index": 47,
            "resting\_heart\_rate": 94,
            "sleep\_balance": 73
        },
        "day": "2021-10-27",
        "score": 66,
        "temperature\_deviation": \-0.2,
        "temperature\_trend\_deviation": 0.1,
        "timestamp": "2021-10-27T00:00:00+00:00"
    },
    ...
\]

### Get Enhanced Tag

[](https://github.com/hedgertronic/oura-ring#get-enhanced-tag)

**Method**: `get_enhanced_tag(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "tag\_type\_code": "string",
        "start\_time": "2019-08-24T14:15:22Z",
        "end\_time": "2019-08-24T14:15:22Z",
        "start\_day": "2019-08-24",
        "end\_day": "2019-08-24",
        "comment": "string"
    },
    ...
\]

### Get Heart Rate

[](https://github.com/hedgertronic/oura-ring#get-heart-rate)

**Method**: `get_heart_rate(start_datetime: str = <end_date - 1 day>, end_datetime: str = <today's date>)`

**Payload**:

*   `start_datetime`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DDThh:mm:ss). Defaults to one day before the `end_datetime` parameter.
*   `end_datetime`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DDThh:mm:ss). Defaults to today's date.

**Example Response**:

\[
    {
        "bpm": 60,
        "source": "sleep",
        "timestamp": "2021-01-01T01:02:03+00:00"
    },
    ...
\]

### Get Sleep Periods

[](https://github.com/hedgertronic/oura-ring#get-sleep-periods)

**Method**: `get_sleep_periods(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "average\_breath": 12.625,
        "average\_heart\_rate": 4.25,
        "average\_hrv": 117,
        "awake\_time": 4800,
        "bedtime\_end": "2022-07-12T09:25:14-07:00",
        "bedtime\_start": "2022-07-12T01:05:14-07:00",
        "day": "2022-07-12",
        "deep\_sleep\_duration": 4170,
        "efficiency": 84,
        "heart\_rate": {
            "interval": 300,
            "items": \[
                None,
                50,
                46,
                ...
            \],
            "timestamp": "2022-07-12T01:05:14.000-07:00"
        },
        "hrv": {
            "interval": 300,
            "items": \[
                None,
                \-102,
                \-122,
                ...
            \],
            "timestamp": "2022-07-12T01:05:14.000-07:00"
        },
        "latency": 540,
        "light\_sleep\_duration": 18750,
        "low\_battery\_alert": False,
        "lowest\_heart\_rate": 48,
        "movement\_30\_sec": "<long sequence of 1|2|3\>",
        "period": 0,
        "readiness\_score\_delta": 0,
        "rem\_sleep\_duration": 2280,
        "restless\_periods": 415,
        "sleep\_phase\_5\_min": "<long sequence of 1|2|3|4\>",
        "sleep\_score\_delta": 0,
        "time\_in\_bed": 30000,
        "total\_sleep\_duration": None,
        "type": "long\_sleep"
    },
    ...
\]

### Get Sleep Time

[](https://github.com/hedgertronic/oura-ring#get-sleep-time)

**Method**: `get_sleep_time(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "day": "2019-08-24",
        "optimal\_bedtime": {
            "day\_tz": 0,
            "end\_offset": 0,
            "start\_offset": 0
        },
        "recommendation": "improve\_efficiency",
        "status": "not\_enough\_nights"
    },
    ...
\]

### Get Ring Configuration

[](https://github.com/hedgertronic/oura-ring#get-ring-configuration)

**Method**: `get_ring_configuration(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "color": "glossy\_black",
        "design": "heritage",
        "firmware\_version": "string",
        "hardware\_type": "gen1",
        "set\_up\_at": "2019-08-24T14:15:22Z",
        "size": 0
    },
    ...
\]

### Get Rest Mode Period

[](https://github.com/hedgertronic/oura-ring#get-rest-mode-period)

**Method**: `get_rest_mode_period(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "end\_day": "2019-08-24",
        "end\_time": "2019-08-24T14:15:22Z",
        "episodes": \[
            {
                "tags": \[
                      "string"
                \],
                "timestamp": "2019-08-24T14:15:22Z"
            }
        \],
        "start\_day": "2019-08-24",
        "start\_time": "2019-08-24T14:15:22Z"
    },
    ...
\]

### Get Sessions

[](https://github.com/hedgertronic/oura-ring#get-sessions)

**Method**: `get_sessions(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "day": "2021-11-12",
        "start\_datetime": "2021-11-12T12:32:09-08:00",
        "end\_datetime": "2021-11-12T12:40:49-08:00",
        "type": "rest",
        "heart\_rate": None,
        "heart\_rate\_variability": None,
        "mood": None,
        "motion\_count": {
            "interval": 5,
            "items": \[
                0
            \],
            "timestamp": "2021-11-12T12:32:09.000-08:00"
        }
    },
    ...
\]

### Get Daily SpO2

[](https://github.com/hedgertronic/oura-ring#get-daily-spo2)

**Method**: `get_daily_spo2(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "day": "2019-08-24",
        "spo2\_percentage": {
            "average": 0
        }
    },
  ...
\]

### Get Daily Stress

[](https://github.com/hedgertronic/oura-ring#get-daily-stress)

**Method**: `get_daily_stress(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "day": "2019-08-24",
        "stress\_high": 0,
        "recovery\_high": 0,
        "day\_summary": "restored"
    },
    ...
\]

### Get Tags

[](https://github.com/hedgertronic/oura-ring#get-tags)

**Method**: `get_tags(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "day": "2021-01-01",
        "text": "Need coffee",
        "timestamp": "2021-01-01T01:02:03-08:00",
        "tags": \[
            "tag\_generic\_nocaffeine"
        \]
    },
    ...
\]

### Get Workouts

[](https://github.com/hedgertronic/oura-ring#get-workouts)

**Method**: `get_workouts(start_date: str = <end_date - 1 day>, end_date: str = <today's date>)`

**Payload**:

*   `start_date`: The earliest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to one day before the `end_date` parameter.
*   `end_date`: The latest date for which to get data. Expected in ISO 8601 format (YYYY-MM-DD). Defaults to today's date.

**Example Response**:

\[
    {
        "id": "8f9a5221-639e-4a85-81cb-4065ef23f979",
        "activity": "cycling",
        "calories": 300,
        "day": "2021-01-01",
        "distance": 13500.5,
        "end\_datetime": "2021-01-01T01:00:00.000000+00:00",
        "intensity": "moderate",
        "label": None,
        "source": "manual",
        "start\_datetime": "2021-01-01T01:30:00.000000+00:00"
    },
    ...
\]

Usage With DataFrame
--------------------

[](https://github.com/hedgertronic/oura-ring#usage-with-dataframe)

Using Oura API data with a Pandas DataFrame is very straightforward:

\>\>\> import pandas as pd

\>\>\> sleep \= client.get\_daily\_sleep()
\>\>\> pd.json\_normalize(sleep)

          day  score                  timestamp  contributors.deep\_sleep  \
0  2022\-09\-01     76  2022\-09\-01T00:00:00+00:00                       99
1  2022\-09\-02     81  2022\-09\-02T00:00:00+00:00                      100

   contributors.efficiency  contributors.latency  contributors.rem\_sleep  \
0                       90                    99                      79
1                       88                    75                      95

   contributors.restfulness  contributors.timing  contributors.total\_sleep
0                        55                   15                        85
1                        56                   28                        96

\[2 rows x 10 columns\]

\>\>\> readiness \= client.get\_daily\_readiness()
\>\>\> pd.json\_normalize(readiness)

          day  score  temperature\_deviation  temperature\_trend\_deviation  \
0  2022\-09\-01     87                  \-0.09                         0.24
1  2022\-09\-02     91                  \-0.03                         0.11

                   timestamp  contributors.activity\_balance  \
0  2022\-09\-01T00:00:00+00:00                             80
1  2022\-09\-02T00:00:00+00:00                             86

   contributors.body\_temperature  contributors.hrv\_balance  \
0                            100                        84
1                            100                        85

  contributors.previous\_day\_activity  contributors.previous\_night  \
0                               None                           75
1                               None                           88

   contributors.recovery\_index  contributors.resting\_heart\_rate  \
0                          100                              100
1                           94                               98

   contributors.sleep\_balance
0                          87
1                          93

\[2 rows x 13 columns\]
