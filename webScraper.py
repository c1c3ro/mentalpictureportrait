import requests
from bs4 import BeautifulSoup

url = "https://tarotfarm.com.br/dez-de-copas-significado-no-tarot/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

soup = soup.find(class_="entry-content")
imageSimbolism = soup.find_all("li")
descriptions = soup.find_all("p")

for i in descriptions:
    print(i.prettify())

for j in imageSimbolism:
    print(j.prettify())