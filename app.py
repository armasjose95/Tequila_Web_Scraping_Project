import requests
from bs4 import BeautifulSoup

url = 'https://www.mysa.wine/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

wineLinks = []
for x in range(1, 4):
    page = requests.get(
        f'https://mysa.wine/collections/natural-wine-store?page={x}')
    soup = BeautifulSoup(page.content, 'html.parser')

    productList = soup.findAll('div', class_="collection__products")

    # print(productList)

    # Iterate over each product in productList to find the 'price' class within each
    """for product in productList:
        # Adjust the class name as needed
        prices = product.find_all(class_='price')
        for price in prices:
            print(price.text.strip())"""

    for wine in productList:
        for link in wine.find_all('a', href=True):
            wineLinks.append(url + link['href'])

# print(wineLinks)
# print(len(wineLinks))


testLink = 'https://mysa.wine/products/les-vins-pirouettes-brutal-de-claude-blanc'
page = requests.get(testLink, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
name = soup.find('h1', class_="product__title heading-size-9").text.strip()
price = soup.find('span', class_='product__price accent-size-5').text.strip()
description = soup.find('p', style_='text-align:center;')
print(name)
print(price)
print(description)
