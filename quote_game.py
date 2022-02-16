#This program scrapes the web page "https://quotes.toscrape.com/" for quotes, and information about people to whom these quotes belong.
# The program then asks the user to guess the person who has said the given quote. Users receive hints when they answer incorrectly.
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
print(celebrity_dict)
