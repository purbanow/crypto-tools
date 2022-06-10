import json
import requests
import pandas as pd

HISTORICAL_DATES_JSON = 'data.json'
HISTORICAL_LISTINGS_URL = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/historical'
HISTORICAL_LISTINGS_LIMIT = 500


def get_historical_dates():
    f = open(HISTORICAL_DATES_JSON)
    data = json.load(f)
    f.close()
    return list(map(lambda date: f"{date[0:4]}-{date[4:6]}-{date[6:8]}", data[0]['historical_dates']))


def get_historical_data(dates):
    result = []
    for date in dates:
        print(f"Starting {date}")
        resp = requests.get(
            url=f"{HISTORICAL_LISTINGS_URL}?convert=USD,BTC&date={date}&limit={HISTORICAL_LISTINGS_LIMIT}&start=1").json()

        if resp['status']['error_message'] is None:
            for crypto in resp['data']:
                crypto['date'] = date
                del crypto['tags']
                del crypto['quote']
                result.append(crypto)
        else:
            print("ERROR")

    return result


dates = get_historical_dates()
data = get_historical_data(dates)

df = pd.DataFrame(data)
df.to_csv('historical_data.csv')
