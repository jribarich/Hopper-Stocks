"""" 
Hopper Stocks:

A Twitter Bot that tweets
information about the top
5 most active stocks on 
the market. This bot tweets 
every 30 minutes while the 
market is open.

By Jack Ribarich

Date Created: August 26th, 2020
"""

import stock_data as sd
import datetime
import twitter
from keys import c_key, c_secret, t_key, t_secret


def convert_time():
	t_zone = 3  # pacific to eastern 

	now = datetime.datetime.now()
	hour = now.hour + t_zone
	minute = now.minute - 1 # for indices starting at 0

	# 9:30 EST = 0 -> 4:00 EST = 390
	new_h = (hour-9)*60 - 30

	return new_h + minute


def active_list():
	now = convert_time()
	past = now - 29  # for indices starting at 0

	stocks = sd.most_active()

	for stock in stocks:
		df = sd.get_df(stock.ticker)

		stock.EMA_20 = sd.get_EMA(df, 20, now)
		stock.EMA_50 = sd.get_EMA(df, 50, now)
		stock.EMA_100 = sd.get_EMA(df, 100, now)

		stock.RSI = sd.get_RSI(df, now, past)

		stock.OBV = sd.get_OBV(df, now, past)

	return stocks


def init_twitter():
	api = twitter.Api(consumer_key= c_key,
                      consumer_secret= c_secret,
                      access_token_key= t_key,
                      access_token_secret= t_secret)

	return api


def main():
	# gather stock data into stock class
	# put into list
	stocks = active_list()

	# initialize twitter w/ API keys
	api = init_twitter()

	# tweet info on each stock
	for i in range(4, -1, -1):
		status = api.PostUpdate(repr(stocks[i]))
		print(status.text)


if __name__ == "__main__":
	main()