from finnhub import Client
import pandas as pd
import time
import datetime


def convert_date(string_date):
    # Accepts a date in the format: '01/12/2011'
    return int(time.mktime(datetime.datetime.strptime(string_date, "%d/%m/%Y").timetuple()))


def request_data(api_key, ticker, start, end):
    client = Client(api_key)
    candles = client.stock_candles(
        ticker,
        'D',
        convert_date(start),
        convert_date(end))
    return candles


def percent_change(start, end):
    return (end - start) / start


def process_candles(candles):
    open_price = candles['o']
    close_price = candles['c']
    return [percent_change(open_price[i], close_price[i]) for i in range(0, len(open_price))]


def get_data(key, symbol, start, end):
    candles = request_data(key, symbol, start, end)
    data = process_candles(candles)
    return pd.Series(data)
