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

testLink = 'https://mysa.wine/products/nestarec-ruz'

# for link in wineLinks:
page = requests.get(testLink, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
"""
name = soup.find('h1', class_="product__title heading-size-9").text.strip()
price = soup.find('span', class_='product__price accent-size-5').text.strip()
#description = set()
#description = soup.findAll('p', style="text-align:center;").text.strip()"""
"""
# Find description under <p> elements
p_description = soup.find_all('p', style="text-align:center;")
p_text = " ".join([p.text.strip() for p in p_description])

# Find description under <h3> elements
h3_description = soup.find_all('h3', style="text-align:center;")
h3_text = " ".join([h3.text.strip() for h3 in h3_description])
"""
justP_description = soup.find('div', class_="tab-content__inner").text.strip()
#justP_text = " ".join([justp.text.strip() for justp in justP_description])

print(justP_description)
