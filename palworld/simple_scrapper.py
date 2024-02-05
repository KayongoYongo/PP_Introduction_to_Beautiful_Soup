#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import json
import os

# Using the requests library to send an HTTP GET request to the and retrieve the HTML content of the webpage. 
source = requests.get('https://palworld.gg/pals').text

# The variable soup will be a BeautifulSoup object that represents the parsed HTML conten
# lxml is a parser
soup = BeautifulSoup(source, 'lxml')

# Find all div elements with class="name" and extract the text
name_divs = soup.find_all('div', class_='name')

# Create a list of the categories for the pals 
category = ['Common', 'Rare', 'Epic', 'Legendary']
pals = []

# Iterate through the name divs and add the pals to a list
pal_categories = {cat: [] for cat in category}

# Iterate through the name divs and add the pals to the corresponding categories
for i in range(0, len(name_divs), 2):
    pal = name_divs[i].get_text(strip=True)
    pal_category = name_divs[i+1].get_text(strip=True)

    pals.append(pal)
    pal_categories[pal_category].append(pal)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the file name for the JSON file in the same directory as the script
file_name = 'pal_categories.json'
file_path = os.path.join(script_dir, file_name)

# JSONify the dictionary
json_data = json.dumps(pal_categories, indent=2)

# Write the JSON data to the file
with open(file_path, 'w') as json_file:
    json_file.write(json_data)

print("All Pals:", pals)
print("Pal Categories:", pal_categories)
