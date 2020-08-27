import ftplib
import io
import json
import pandas
import requests
import requests_html
import yahoo_fin.stock_info as si
import yfinance as yf
from technical_indicators_lib import EMA, RSI, OBV


class Stock():
	def __init__(self):
		self.rank = None  # most active rank
		self.name = None
		self.ticker = None
		self.price = None
		self.per_change = None
		self.EMA_20 = None
		self.EMA_50 = None  
		self.EMA_100 = None
		self.RSI = None  # 30min diff
		self.OBV = None  # 30min diff


def most_active():
	stock_lst = []

	most_active = si.get_day_most_active()

	for x in range(5):
		stock = Stock()

		stock.rank = x + 1
		stock.ticker = most_active['Symbol'][x]
		stock.company = most_active['Name'][x]
		stock.price = most_active['Price (Intraday)'][x]
		stock.per_change = most_active['% Change'][x]

		stock_lst.append(stock)

	return stock_lst


def get_df(ticker):
	df = yf.download(tickers = ticker, period = '1d', interval = '1m')
	df.columns = df.columns.str.lower()  # have to make columns lowercase

	return df


def get_EMA(df, period):
	ema = EMA()  # Exponential Moving Average

	ema_df = ema.get_value_df(df, period)
	print(ema_df['EMA'])
	return 0


def get_RSI(df):
	rsi = RSI()  # Relative Strength Index

	rsi_df = df[['close']].fillna(0)  # fill NAN values with 0
	rsi_df = rsi.get_value_df(rsi_df, 14)

	print(rsi_df['RSI']) #delete

	return 0


def get_OBV(df):
	obv = OBV()  # # On Balance Volume

	obv_df = obv.get_value_df(df)

	print(obv_df['OBV'])  #delete

	return 0