import requests
from bs4 import BeautifulSoup
import json
import random
url = 'https://economictimes.indiatimes.com/markets'  # Replace with the URL of the website you want to scrape

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all anchor tags with text length greater than 10 characters
anchor_tags = soup.find_all('a', string=lambda string: string and len(string) > 35)
anchor_data = []
# Extract and print the href attribute and text of the selected anchor tags
for anchor in anchor_tags:
    href = anchor.get('href')
    text = anchor.text
    anchor_data.append({
        'text': text,
        'link': href
    })
random.shuffle(anchor_data)
# Write the extracted data to output.json file
with open('/Users/mukeshpatel/Documents/5th SEMESTER/Python/Project/chart/public/news.json', 'w') as json_file:
    json.dump(anchor_data, json_file, indent=4)
