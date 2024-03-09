import requests
from bs4 import BeautifulSoup

url = 'https://www.binnys.com/'


headers = [{
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}]


page = requests.get(
    'https://www.binnys.com/spirits/tequila/?refinementList%5BproductVarietal%5D%5B0%5D=Blanco')
soup = BeautifulSoup(page.content, 'html.parser')


productList = soup.find_all('div', class_='product-item')

print(productList)
