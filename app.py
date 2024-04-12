# import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.mysa.wine/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

wineLinks = set()
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
            wineLinks.add(url + link['href'])

# print(wineLinks)
# print(len(wineLinks))

# testLink = 'https://mysa.wine/products/cal-xurriu-instint-animal-blanc'

for link in wineLinks:
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # name = soup.find('div', class_="product__title__wrapper").text.strip()
    name_element = soup.find('h1', class_="product__title heading-size-9")
    if name_element is not None:
        name = name_element.text.strip()
    else:
        name = "Unknown"

    # price = soup.find('span', class_='product__price accent-size-5').text.strip()

    price_element = soup.find('h1', class_="product__price accent-size-5")
    if price_element is not None:
        price = price_element.text.strip()
    else:
        price = "Unknown"

    # description = soup.find('div', class_="tab-content__inner").text.strip()

    description_element = soup.find('div', class_="tab-content__inner")
    if description_element is not None:
        description = description_element.text.strip()
    else:
        description = "Unknown"

    drink = {
        'name': name,
        'price': price,
        'description': description
    }

    """# Remove any non-numeric characters from the price text and convert it to a float
    priceTextToNum = float(''.join(filter(str.isdigit, price))) / 100
    if priceTextToNum < 26:
        print(drink)
        # productList.append(drink)"""

    # Remove non-numeric characters from the price text
    cleaned_price_text = ''.join(filter(str.isdigit, price))
    # Convert the cleaned price text to a float (assuming the price is in cents)
    try:
        price_in_cents = float(cleaned_price_text) / 100
    except ValueError:
        price_in_cents = None  # or some default value

    # Check if the price is less than $25 before printing the drink
    if price_in_cents is not None and price_in_cents < 25:
        print(drink)


# df = pd.DataFrame(productList)
