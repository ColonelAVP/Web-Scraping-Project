# This file consists of code to scrape data from website named quotes to scrape.
# Packages used:
import requests
from bs4 import BeautifulSoup
from csv import DictWriter

# Scraping data from the URL below.
BASE_URL = "http://quotes.toscrape.com/"

def scrape_quotes():
    all_quotes = []
    page_url = "/page/1"
    while page_url:
        response = requests.get(f"{BASE_URL}{page_url}")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_ ="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "link": quote.find("a")["href"]
            })
            next_btn = soup.find(class_="next")
            page_url = next_btn.find("a")["href"] if next_btn else None
    return all_quotes

def write_csv(quotes):
    with open("quotes1.csv","w",encoding="UTF-8") as file:
        headers = ["text","author","link"]
        csv_writer = DictWriter(file,fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_csv(quotes)
