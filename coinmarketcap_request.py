import urllib.request
import os
import datetime
import time

if not os.path.exists("midterm_html_files"):
	os.mkdir("midterm_html_files")

# for i in range():
current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
print(current_time_stamp)
f = open("midterm_html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
coin_market_response = urllib.request.urlopen("https://coinmarketcap.com/")
coin_market_html = coin_market_response.read()

f.write(coin_market_html)
f.close()

time.sleep(15)

current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
print(current_time_stamp)
f = open("midterm_html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
coin_market_response = urllib.request.urlopen("https://coinmarketcap.com/2")
coin_market_html = coin_market_response.read()

f.write(coin_market_html)
f.close()

time.sleep(15)

current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
print(current_time_stamp)
f = open("midterm_html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
coin_market_response = urllib.request.urlopen("https://coinmarketcap.com/3")
coin_market_html = coin_market_response.read()

f.write(coin_market_html)
f.close()

time.sleep(15)

current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
print(current_time_stamp)
f = open("midterm_html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
coin_market_response = urllib.request.urlopen("https://coinmarketcap.com/4")
coin_market_html = coin_market_response.read()

f.write(coin_market_html)
f.close()

time.sleep(15)

current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
print(current_time_stamp)
f = open("midterm_html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
coin_market_response = urllib.request.urlopen("https://coinmarketcap.com/5")
coin_market_html = coin_market_response.read()

f.write(coin_market_html)
f.close()
