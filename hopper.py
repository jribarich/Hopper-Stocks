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


def active_list():
	stocks = sd.most_active()

	for stock in stocks:
		df = sd.get_df(stock.ticker)

		stock.EMA_20 = sd.get_EMA(df, 20)
		stock.EMA_50 = sd.get_EMA(df, 50)
		stock.EMA_100 = sd.get_EMA(df, 100)

		stock.RSI = sd.get_RSI(df)

		stock.OBV = sd.get_OBV(df)

	return stocks
	
	
def main():
	# gather stock data into a list
	# of stock instances
	stocks = active_list()
	# put each stock into a class

	# tweet info on each stock


if __name__ == "__main__":
	main()