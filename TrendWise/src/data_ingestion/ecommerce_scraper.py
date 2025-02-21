import requests
from bs4 import BeautifulSoup

def scrape_ecommerce_trends():
    url = "https://www.amazon.com/best-sellers/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.p13n-sc-truncate'):
        products.append(item.get_text(strip=True))

    return products
