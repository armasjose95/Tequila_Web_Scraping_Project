import requests
from bs4 import BeautifulSoup

url = 'https://www.mysa.wine/'


headers = [{
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}]


page = requests.get(
    'https://mysa.wine/collections/orange-natural-wine-online')
soup = BeautifulSoup(page.content, 'html.parser')


productList = soup.findAll('div', class_="collection__products")

# print(productList)

# Iterate over each product in productList to find the 'price' class within each
for product in productList:
    price = product.find_all(class_='price')  # Adjust the class name as needed
    print(price)


#price = productList.find('price')
# print(price)
