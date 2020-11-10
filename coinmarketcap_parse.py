from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("midterm_parsed_files"):
	os.mkdir("midterm_parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("midterm_html_files/*.html"):
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html","")
	f = open(one_file_name, "r", encoding = "utf-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	currencies_table = soup.find("tbody")
	currency_rows = currencies_table.find_all("tr")

	for r in currency_rows:
		currency_columns = r.find_all("td")
		if len(currency_columns)>10:
			currency_price = currency_columns[3].find("a", {"class": "cmc-link"}).text.replace("$","").replace(",","")
			currency_logo = currency_columns[2].find("img")
			currency_name = currency_columns[2].find("p").text
			currency_trading_volume = currency_columns[7].find("p").text
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_24hr_growth = currency_columns[4].find("span").text
			currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace(",","")
			currency_link = currency_columns[2].find("a")["href"]
			df = df.append({
					'name': currency_name,
					'price': currency_price,
					'trading volume': currency_trading_volume,
					'marketcap': currency_marketcap,
					'symbol': currency_symbol,
					'logo': currency_logo,
					'link': currency_link,
					'24hr growth': currency_24hr_growth,
					'time': scrape_time
				}, ignore_index=True)


df.to_csv("midterm_parsed_files/coinmarketcap_dataset.csv")