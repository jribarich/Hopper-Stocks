import numpy as np
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
		self.RSI = None 
		self.OBV = None  # 30min diff

	def __repr__(self):
		string = f"""{self.rank}. {self.ticker} {self.price} ({self.per_change}%)

   EMA (20): {self.EMA_20}
   EMA (50): {self.EMA_50}
   EMA (100): {self.EMA_100}

   RSI: {self.RSI}
   OBV: {self.OBV}
		"""

		return string


def most_active():
	stock_lst = []

	most_active = si.get_day_most_active()

	for x in range(5):
		stock = Stock()

		stock.rank = x + 1
		stock.ticker = most_active['Symbol'][x]	
		stock.company = most_active['Name'][x]
		# '%+.2f' % gives a +/- and round to 2 dec. places
		stock.price = '%.2f' %(most_active['Price (Intraday)'][x])
		stock.per_change = '%+.2f' %(most_active['% Change'][x])

		stock_lst.append(stock)

	return stock_lst


def get_df(ticker):
	df = yf.download(tickers = ticker, period = '1d', interval = '1m')
	df.columns = df.columns.str.lower()  # have to make columns lowercase
	df.set_index(np.arange(len(df)))  # sets indices instead of datenow

	return df


def get_EMA(df, period, now):
	ema = EMA()  # Exponential Moving Average

	ema_df = ema.get_value_df(df, period)
	out = ema_df['EMA'].iloc[now]  # output

	out = '%.2f' %(out)  # rounds to 2 dec. places

	return out


def get_RSI(df, now, past):
	rsi = RSI()  # Relative Strength Index

	rsi_df = df[['close']].fillna(0)  # fill NAN values with 0
	rsi_df = rsi.get_value_df(rsi_df, 14).fillna(0)

	new = rsi_df['RSI'].iloc[now]
	old = rsi_df['RSI'].iloc[past]
	diff = new - old

	out = '%+d' %(diff)  # adds a +/- to num

	return out


def get_OBV(df, now, past):
	obv = OBV()  # On Balance Volume

	obv_df = obv.get_value_df(df)

	new = obv_df['OBV'].iloc[now]
	old = obv_df['OBV'].iloc[past]
	diff = new - old

	out = '%+d' %(diff)  # adds a +/- to num

	return out