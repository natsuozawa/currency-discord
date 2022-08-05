# currency-discord

Notifies a discord channel via webhook about currency rates using a custom mechanism.

# Background

Managing finances in multiple currencies can be hectic. I have created this workflow to spare the time of searching exchange rates every month.

# Mechanism

This workflow calculates a roughly stable exchange rate by taking the average daily exchange rate of the last n days (this is configurable, up to 365). You can configure a periodic activation of this workflow using crontab.

Depends on [fawazahmed0/currency-api](https://github.com/fawazahmed0/currency-api).

# Installation and configuration

Developed and tested using Python 3.9.

Create an .env file from .env.example as follows:

```
WEBHOOK_URL= obtained from Discord.
CURRENCIES_FORM= comma separated values, ISO abbreviations
CURRENCIES_TO= comma separated values, ISO abbreviations
LAST_N_DAYS= number from 1 to 365
```

This workflow will generate currency rates for all currency pairs in `CURRENCIES_FORM` and `CURRENCIES_TO`.

Then, run

```
docker-compose up
```

# Development

After cloning the repository, create and use a virtual environment.

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies.

```
pip3 install -r requirements.txt
```
