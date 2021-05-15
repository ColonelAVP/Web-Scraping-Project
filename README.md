# Web-Scraping-Project
## Introduction
In this project you'll be building a quotes guessing game. We have used a special library named Beautiful soup. 
When run, your program will scrape a website for a collection of quotes. 
Pick one at random and display it. The player will have four chances to guess who said the quote. 
After every wrong guess they'll get a hint about the author's identity.

Concept used in this project:
* Web Scraping

Tools and Technology used:
* Python
* Beautiful Soup for extracting data from HTML
* Requests to make HTTP requests


### Note 
Before starting with the steps, one important thing. 
For the purspose of Web scraping, Ideally it is recommended to use websites that allow you to scrape data.
Not every websites take action, but there are some which may get you banned. So check websites before using.

> Installation Guide
> pip install beautifulsoup4
  
## Steps
```Python
Step1: Create a file called `scrape_data.py` which, when run, grabs data on every quote from the website.
Step2: You can use `bs4` and `requests` to get the data. 
       For each quote you should grab the following;
       - text of the quote, 
       - the name of the person who said the quote, 
       - the href of the link to the person's bio. 
Step3: Store all of this information in a list.
Step4: Display the quote to the user and ask who said it. The player will have four guesses remaining.
Step5: After each incorrect guess, the number of guesses remaining will decrement. 
Step6: If the player gets to zero guesses without identifying the author, the player loses and the game ends. 
Step7: If the player correctly identifies the author, the player wins!
Step8: After every incorrect guess, the player receives a hint about the author. 
Step9: For the first hint, make another request to the author's bio page (this is why we originally scrape this data), 
        and tell the player the author's birth date and location.
Step10: The next two hints are up to you! 
        Some ideas: 
         - the first letter of the author's first name,
         - the first letter of the author's last name, 
         - the number of letters in one of the names, etc.
Step11. When the game is over, ask the player if they want to play again. 
        * If yes, restart the game with a new quote. 
        * If no, the program is complete.
```

## Reference
**Used Website** ==> [Quotes-to-Scrape](http://quotes.toscrape.com/)
I have also uploaded the csv file, in which I've stored the scraped data [qoutes1.csv](https://github.com/ColonelAVP/Web-Scraping-Project/blob/master/quotes1.csv):
