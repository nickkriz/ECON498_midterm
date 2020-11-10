from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("midterm_parsed_g_files"):
	os.mkdir("midterm_parsed_g_files")

df = pd.DataFrame()

one_file_name = "midterm_html_g_files/coinrank20201110160810.html"
print(one_file_name)
scrape_time = os.path.basename(one_file_name).replace("coinrank","").replace(".html","")
f = open(one_file_name, "r", encoding = "utf-8")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

currencies_table = soup.find("tbody", {"class": "table_body"})
currency_rows = currencies_table.find_all("tr")

for one_file_name in glob.glob("midterm_html_g_files/*.html"):
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("coinrank","").replace(".html","")
	f = open(one_file_name, "r", encoding = "utf-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	currencies_table = soup.find("tbody")
	currency_rows = currencies_table.find_all("tr")

	for r in currency_rows:
		currency_columns = r.find_all("td")
		if len(currency_columns)>10:
			currency_name = currency_columns[2].find("span", {"class": "profile_link"}).text
			currency_price = currency_columns[3].find("div", {"class": "valuta valuta--light"}).text.replace("$","").replace(",","")
			currency_logo = currency_columns[2].find("img")
			currency_symbol = currency_columns[2].find("span", {"class": "profile_subtitle"}).text
			currency_24hr_growth = currency_columns[5].find("div", {"class": "change change--light change--negative"}).text
			currency_marketcap = currency_columns[4].find("div", {"class": "valuta valuta--light"}).text.replace("$","").replace(",","")
			currency_link = currency_columns[2].find("span")["href"]
			df = df.append({
					'name': currency_name,
					'price': currency_price,
					'marketcap': currency_marketcap,
					'symbol': currency_symbol,
					'logo': currency_logo,
					'link': currency_link,
					'24hr growth': currency_24hr_growth,
					'time': scrape_time
				}, ignore_index=True)


df.to_csv("midterm_parsed_files/coinmarketcap_dataset.csv")
		