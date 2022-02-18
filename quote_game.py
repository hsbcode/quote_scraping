#This program scrapes the web page "https://quotes.toscrape.com/" for quotes, and information about people to whom these quotes belong.
# The program then asks the user to guess the person who has said the given quote. Users receive hints when they answer incorrectly.
from random import choice
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
quote_celebrity_dict = {}
celebrity_dict = {}
quotes = soup.find_all(class_="quote")
for quote in quotes:
    quote_celebrity_dict [quote.find(class_="text").get_text()] = quote.find(class_ = "author").get_text()
    if quote.find(class_ = "author").get_text() not in celebrity_dict.keys():
        new_list = []
        author_url = url + quote.find("a")["href"]
        author_request = requests.get(author_url)
        author_soup = BeautifulSoup(author_request.text, "html.parser")
        new_list.append(author_soup.find(class_="author-born-date").get_text())
        new_list.append(author_soup.find(class_="author-born-location").get_text())
        author_name = quote.find(class_ = "author").get_text()
        author_name_splitted = author_name.split(" ")
        author_initials = [i[0] for i in author_name_splitted]
        new_list.append(author_initials)
        celebrity_dict[quote.find(class_ = "author").get_text()] = new_list

        
counter = 2

while soup.find(class_="next"):
    next_url = "https://quotes.toscrape.com/page/"+str(counter)+"/"
    request = requests.get(next_url)
    soup = BeautifulSoup(request.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        quote_celebrity_dict [quote.find(class_="text").get_text()] = quote.find(class_ = "author").get_text()
        if quote.find(class_ = "author").get_text() not in celebrity_dict.keys():
            new_list = []
            author_url = url + quote.find("a")["href"]
            author_request = requests.get(author_url)
            author_soup = BeautifulSoup(author_request.text, "html.parser")
            new_list.append(author_soup.find(class_="author-born-date").get_text())
            new_list.append(author_soup.find(class_="author-born-location").get_text())
            author_name = quote.find(class_ = "author").get_text()
            author_name_splitted = author_name.split(" ")
            author_initials = [i[0] for i in author_name_splitted]
            new_list.append(author_initials)
            celebrity_dict[quote.find(class_ = "author").get_text()] = new_list
    counter += 1
#Game Logic
continues = False
while not continues: 
    random_quote_celebrity_pair = choice(list(quote_celebrity_dict.items()))

    print("Here is your quote: " + random_quote_celebrity_pair[0])
    user_input = input("Can you guess who said it? Try 1/4: ")
    if user_input == random_quote_celebrity_pair[1]:
        print("Hurray, you guessed correctly!")
    else:
        print("Oops that was incorrect :(")
        print(f"Hint 1/3 : The celebrity was born in {celebrity_dict[random_quote_celebrity_pair[1]][0]}.")
        user_input = input("Can you guess who said it? Try 2/4: ")
        if user_input == random_quote_celebrity_pair[1]:
            print("Hurray, you guessed correctly!")
        else:
            print("Oops that was incorrect :(")
            print(f"Hint 2/3 : The celebrity was born in {celebrity_dict[random_quote_celebrity_pair[1]][1]}.")
            user_input = input("Can you guess who said it? Try 3/4: ")
            if user_input == random_quote_celebrity_pair[1]:
                print("Hurray, you guessed correctly!")
            else:
                print("Oops that was incorrect :(")
                print(f"Hint 3/3 : The celebrity has the initials {celebrity_dict[random_quote_celebrity_pair[1]][2]}.")
                user_input = input("Can you guess who said it? Try 4/4: ")
                if user_input == random_quote_celebrity_pair[1]:
                    print("Hurray, you guessed correctly!")
                else:
                    print(f"Sorry you lost! The correct answer was {random_quote_celebrity_pair[1]}.J")
    replay_input = input("Do you want to play again y/n?").lower()
    if replay_input == "n":
        continues = True
