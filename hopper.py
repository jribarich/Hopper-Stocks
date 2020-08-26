import ftplib
import io
import json
import pandas
import requests
import requests_html
import yahoo_fin.stock_info as si
import yfinance as yf
from technical_indicators_lib import MACD, RSI, MOM, OBV


most_active = si.get_day_most_active()
print(most_active[:5])


tickers = [most_active['Symbol'][x] for x in range(5)]
company = [most_active['Name'][x] for x in range(5)]
prices = [most_active['Price (Intraday)'][x] for x in range(5)]
per_change = [most_active['% Change'][x] for x in range(5)]


print(company)
print(tickers)
print(prices)
print(per_change)


# Now that we have tickers, lets get the data from yfinance of just one company
#using Yfinance cause it has smaller time scale

aapl = yf.download(tickers = tickers[0], period = '1d', interval = '1m')

print(aapl)


# # MACD Test
df = aapl
df.columns = df.columns.str.lower()  # have to make columns lowercase
macd = MACD()
macd_df = macd.get_value_df(df, 12, 26, True, 9)


# RSI Test

rsi = RSI()
new = df[['close']].fillna(0)  # fill NAN works for some reason
rsi_df = rsi.get_value_df(new, 14)

print(rsi_df)


# OBV Test
obv = OBV()  # obv
obv_df = obv.get_value_df(df)

print(obv_df)



#MOM Test

mom = MOM()  # obv
mom_df = mom.get_value_df(new)

print(mom_df)