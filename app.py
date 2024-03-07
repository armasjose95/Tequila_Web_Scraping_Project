import requests
from bs4 import BeautifulSoup

url = 'https://www.binnys.com/'
page = requests.get(url)

headers = [{
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}]
