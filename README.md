# Oura Ring for Python

Tools for acquiring and analyzing Oura API data.

[Oura](https://ouraring.com/) is a wearable ring for monitoring sleep, activity, and workouts.

## Installation

The `oura_ring` module can be installed via pip:

```bash
pip install oura-ring
```

## Getting Started

In order to use the Oura client, you must first generate a [`personal_access_token`](https://cloud.ouraring.com/personal-access-tokens) for your Oura account.

It is best practice to store this value in a `.env` file:

```
# Oura credentials
PERSONAL_ACCESS_TOKEN="<PERSONAL_ACCESS_TOKEN>"
```

You can use [`python-dotenv`](https://github.com/theskumar/python-dotenv) to load the environment variables for use in code:

```python
import os
from dotenv import load_dotenv

load_dotenv()

pat = os.getenv("PERSONAL_ACCESS_TOKEN") or ""
```

Once the environment variables are loaded, an `OuraClient` object can be created:

```python
from oura_ring import OuraClient

# Using a traditional constructor
client = OuraClient(pat)
...

# Using a context manager
with OuraClient(pat) as client:
    ...
```

## API Functionality

This package provides access to the Oura Ring API v2 including endpoints for:

- Personal Info
- Daily Sleep
- Daily SpO2
- Daily Stress
- Daily Activity
- Daily Readiness
- Enhanced Tags
- Heart Rate
- Ring Configuration
- Rest Mode Period
- Sleep Periods
- Sleep Time
- Sessions
- Tags
- Workouts

See the [documentation](docs/oura-ring-docs.md) for detailed API information.
