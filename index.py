import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1"

"""
Create currency pairs given 2 currency comma separated strings.
"""
def create_pairs(currencies_from, currencies_to):
  left = currencies_from.split(',')
  right = currencies_to.split(',')
  currency_pairs = []
  for l in left:
    for r in right:
      if l == r:
        continue
      currency_pairs.append((l, r))
  return currency_pairs

"""
Given currency pair lists of format [("cur1", "cur2"), ("cur3", "cur4"), ...]
and a date string in format "YYYY-MM-DD"
Return the exchange rate in decimal value.
"""
def find_rates(currency_pairs, dates):
  rates = []
  for (left, right) in currency_pairs:
    daily_rates = []
    for date in dates:
      endpoint = f'{API_URL}/{date}/currencies/{left.lower()}/{right.lower()}.json'
      r = requests.get(endpoint)
      if r.status_code == 200:
        res = r.json()
        daily_rates.append(res[right])
      else:
        raise Exception('API request failed. Please retry.')
    mean_rate = sum(daily_rates) / len(daily_rates)
    rates.append(f'1 {left.upper()} = {mean_rate} {right.upper()}')
  return rates

"""
List of the n most recent days.
"""
def recent_days(n):
  today = datetime.date.today()
  return [str(today - datetime.timedelta(days=i)) for i in range(n)]

def send_webhook(message):
  payload = {
    'content': message,
  }
  r = requests.post(os.environ['WEBHOOK_URL'], json=payload)
  if r.status_code != 204:
    raise Exception('Webhook request failed. Please retry.')

"""
Run the workflow.
"""
def run():
  currency_pairs = create_pairs(os.environ['CURRENCIES_FROM'], os.environ['CURRENCIES_TO'])
  n = int(os.environ['LAST_N_DAYS'])
  if n < 0 or n > 365:
    raise Exception('Invalid last number of days value.')
  ans = find_rates(currency_pairs, recent_days(n))
  rates = '\n'.join(ans)
  date_end = recent_days(n)[0]
  date_begin = recent_days(n)[6]
  message = f'Averaged exchange rates from {date_begin} to {date_end}\n{rates}'
  send_webhook(message)

if __name__ == "__main__":
  run()

