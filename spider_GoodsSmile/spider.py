import requests
import re
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_page(html):
    # htmls = html.text
    soup = BeautifulSoup(html, 'html.parser')
    # hitBox = soup.find(class_="hitList clearfix")
    hitBox = soup.find(class_="cf")
    for i in hitBox.find_all(name='a', attrs={"href":re.compile(r'^https:')}):
        print(i['href'])


def main():
    url = 'https://www.goodsmile.info/zh/products/announced/2019'
    html = get_page(url)
    parse_page(html)


if __name__ == '__main__':
    main()