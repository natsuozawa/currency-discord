# currency-discord

Notifies a discord channel via webhook about currency rates using a custom mechanism.

# Background

Managing finances in multiple currencies can be hectic. I have created this bot to spare the time of searching exchange rates every month.

# Mechanism

This bot calculates a roughly stable exchange rate by taking the average daily exchange rate of the last 7 days. This bot sends a currency rate notification to Discord on the 1st and 15th day of every month using Discord webhooks.

Depends on [fawazahmed0/currency-api](https://github.com/fawazahmed0/currency-api).

# Installation

Developed and tested using Python 3.9.

# Configuration

Create an .env file from .env.example as follows:

```json
WEBHOOK_URL= obtained from Discord.
CURRENCIES_FORM= comma separated values, ISO abbreviations
CURRENCIES_TO= comma separated values, ISO abbreviations
```

This workflow will generate currency rates for all currency pairs in `CURRENCIES_FORM` and `CURRENCIES_TO`.

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
