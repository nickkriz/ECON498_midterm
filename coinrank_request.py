import urllib.request
import os
import datetime
import time

if not os.path.exists("midterm_html_g_files"):
	os.mkdir("midterm_html_g_files")

for i in range(10):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=2")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=3")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=4")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=5")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=6")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=2")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=7")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=8")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=9")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("midterm_html_g_files/coinrank" + current_time_stamp + ".html", "wb")
	coin_rank_response = urllib.request.urlopen("https://coinranking.com/?page=10")
	coin_rank_html = coin_rank_response.read()

	f.write(coin_rank_html)
	f.close()

	time.sleep(15)
		
# time.sleep(15)