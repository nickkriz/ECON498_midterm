from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("midterm_parsed_g_files"):
	os.mkdir("midterm_parsed_g_files")

df = pd.DataFrame()

one_file_name = "coinrank20201110185412.html"
print(one_file_name)
scrape_time = os.path.basename(one_file_name).replace("coinrank","").replace(".html","")
f = open(one_file_name, "r", encoding = "utf-8")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

currencies_table = soup.find("tbody")
currency_rows = currencies_table.find_all("tr")

for r in currency_rows:
	currency_columns = r.find_all("td")
	if len(currency_columns)>3:
		print(currency_columns[0])
		currency_name = currency_columns[0].find("a").text
		currency_price = currency_columns[1].find("div", {"class": "valuta valuta--light"}).text.replace("$","").replace(",","")
		currency_symbol = currency_columns[0].find("span", {"class": "profile__subtitle"}).text
		currency_24hr_growth = currency_columns[3].find("div", {"class": "change"}).text
		currency_marketcap = currency_columns[2].find("div", {"class": "valuta valuta--light"}).text.replace("$","").replace(",","")
		currency_link = currency_columns[0].find("a")["href"]
		df = df.append({
				'name': currency_name,
				'price': currency_price,
				'marketcap': currency_marketcap,
				'symbol': currency_symbol,
				'link': currency_link,
				'24hr growth': currency_24hr_growth,
				'time': scrape_time
			}, ignore_index=True)


df.to_csv("midterm_parsed_g_files/coinrank_dataset.csv")