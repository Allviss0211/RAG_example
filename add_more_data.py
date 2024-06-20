import json
import os
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient, InsertOne
import pymongo

# Connection to the MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')
DB_NAME = os.getenv('DB_NAME')
DB_COLLECTION = os.getenv('DB_COLLECTION')
client = pymongo.MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[DB_COLLECTION]
requesting = []

files = ['iphone', 'samsung', 'xiaomi']

for file in files:
    with open(f'data/{file}.json','r', encoding='utf-8') as f:
        myDict = json.load(f)
        for item in myDict['items']:

            # URL of the web page you want to scrape
            url = item['url']

            # Send a request to the web page
            response = requests.get(url)

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the div with the class "product-option color"
            colors_div = soup.find('div', class_='product-option color')

            list_color = []

            # Loop through the list of divs
            for div in colors_div.find_all('div', class_=['item']):
                # Find the span with the class "color-name"
                list_color.append(div.get('data-name'))

            item['color_options'] = list_color
            item.pop('color')

            # Find the div with the class "product-promotion"
            promotion_div = soup.find('div', class_='product-promotion')

            # Find the li and spilt 2 li is 1 pair promotion connect with dash
            list_promotion = promotion_div.find_all('li')
            #trim text
            list_promotion = [li.text.strip() for li in list_promotion]

            # join pair item with dash
            list_promotion = [' - '.join(list_promotion[i:i+2]) for i in range(0, len(list_promotion), 2)]

            item['promotions'] = list_promotion

            #check if unit_price null will set unit_sale_price
            if item['unit_price'] == None:
                item['unit_price'] = item['unit_sale_price']

            requesting.append(InsertOne(item))
            name = item['name']
            print(f'---------{name}--DONE----------')

result = collection.bulk_write(requesting)
client.close()