# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://ya.ru'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)