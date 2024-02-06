#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import string
import csv

with open("all_UFC_figters.csv", "w", newline='', encoding='utf-8') as file_results:
    writer = csv.writer(file_results)
    writer.writerow(["First name", "Last name", "Nickname","Height","Weight","Reach","Stance", "W","L","D","BELT"])
    
    # Base url
    base_url = "http://www.ufcstats.com/statistics/fighters?char="

    # Get all uppercase letters from A to Z
    letters = string.ascii_uppercase

    for letter in letters:
        # Modify the url to iterate from A to Z
        url = base_url + letter + "&page=all"
        # Use the requests library to send a HTTP GET requestto the page and retrieve the content of the webpage
        response = requests.get(url)

        # The variable soup will be a BeautifulSoup object that represents the parsed HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all table rows
        rows = soup.find_all('tr', class_='b-statistics__table-row')

        # Iterate over each row
        for row in rows:
            # Find all table data cells in the rows
            cells = row.find_all('td', class_='b-statistics__table-col')

            if len(cells) >= 11:
                # Extract the cell from each cell and print
                first_name = cells[0].text.strip()
                last_name = cells[1].text.strip()
                nick_name = cells[2].text.strip()
                height = cells[3].text.strip()
                weight = cells[4].text.strip()
                reach = cells[5].text.strip()
                stance = cells[6].text.strip()
                W = cells[7].text.strip()
                L = cells[8].text.strip()
                D = cells[9].text.strip()
                belt = cells[10].text.strip()
                writer.writerow([first_name, last_name, nick_name, height, weight, reach, stance, W, L, D, belt])
            else:
                continue
    print("Task successful")
