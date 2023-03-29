from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://www.kivano.kg/kompyutery"

HEADERS = {
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url=url)
    return response


def get_data_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(
        'div', class_="item product_listbox oh"
    )
    products = []
    for item in items:
        product = {
            "title": item.find('div', class_="listbox_title oh").getText().replace("\n", ""),
            "link": item.find('div', class_="listbox_title oh").find('a').get('href').replace("\n", ""),
            "price": item.find('div', class_="listbox_price text-center").getText().replace("\n", "")
        }
        products.append(product)
    pprint(products)


html = get_html(URL)
get_data_from_page(html.text)
