import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

def get_url():

    for count in range(1,8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"


        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

        for i in data:
            card = "https://scrapingclub.com" + i.find("a").get("href")
            yield card


def array():
    for product in get_url():

        response = requests.get(product, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find("div", class_="card mt-4 my-4")
        title = data.find('h3', class_="card-title").text
        price = data.find('h4').text
        description = data.find('p', class_="card-text").text
        image = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get('src')
        yield title, price, description, image