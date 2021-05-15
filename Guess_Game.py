# this file consists of the code of game made using scraped data from file [Scraped_data.py]
# Packages and libraries used:
import requests
from random import choice
from bs4 import BeautifulSoup
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename,"r",encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    guess_left = 4
    print("Here's a quote: ")
    print(quote["text"])
    guess = ""
    while guess.lower() != quote["author"].lower() and guess_left > 0:
        guess = input(f"Who said this quote?....Guesses remaining {guess_left}")
        if guess.lower() == quote["author"].lower():
            print("Excellent,You Got it right!!!")
        else:
            guess_left -= 1
            if guess_left == 3:
                response = requests.get(f"{BASE_URL}{quote['link']}")
                soup = BeautifulSoup(response.text, "html.parser")
                birth_date = soup.find(class_="author-born-date").get_text()
                birth_place = soup.find(class_="author-born-location").get_text()
                print(f"Here's a hint....The author was born on {birth_date} {birth_place}")
            elif guess_left == 2:
                print(f"Another hint... The author's first name starts with {quote['author'][0]}")
            elif guess_left == 1:
                last_initial = quote["author"].split(" ")[1][0]
                print(f"Last Hint.....The author's last name starts with {last_initial}")
            else:
                print(f"You ran out of guesses....The answer was {quote['author']}")

    again = ''
    while again.lower() not in ("yes","y","no","n"):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ("yes","y"):
        print("OK, Lets play")
        return start_game(quotes)
    else:
        print("OK, Goodbye!!")

quotes = read_quotes("quotes1.csv")
start_game(quotes)
