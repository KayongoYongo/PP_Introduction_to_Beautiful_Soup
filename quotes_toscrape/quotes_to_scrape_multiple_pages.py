#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv

for page_number in range(1, 10):
    url = f"https://quotes.toscrape.com/page/{page_number}"
    # Using the requests library to send an HTTP GET request to the and retrieve the HTML content of the webpage
    response = requests.get(url)

    # The variable soup will be a BeautifulSoup object that represents the parsed HTML conten
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all div elements with class="name" and extract the text
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # Write the results onto a CSV file
    file_results = open("scraped_quotes_page_10.csv", "w")
    writer = csv.writer(file_results)

    writer.writerow(["Quotes", "Authors"])

    for quote, author in zip(quotes, authors):
        print(quote.text + " - " + author.text)
        writer.writerow([quote.text, author.text])
    file_results.close()
