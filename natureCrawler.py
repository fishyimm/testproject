import requests
from bs4 import BeautifulSoup


def crawler(max_page):
    page = 1
    while page <= max_page:
        url = "http://www.snipertopanime.net/index.php?page=" + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.find_all('div', {'class': 'anime-title'}):
            href = "http://www.snipertopanime.net/" + link.a.get('href')
            get_single_item_data(href)
            print(link.a.string)
            print(link.a.get('href'))
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.find_all('meta', {'name': 'keywords'}):
        print(item_name.attrs)
        print(item_name.attrs['content'])
        print("------------------- End -----------------------------")

crawler(2)

