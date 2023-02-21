import requests
import json
from bs4 import BeautifulSoup


def get_card_content(title, url):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    ids = []
    labels = []
    content = {"card": title,
            "contents": {}}
    
    
    p1 = soup.find("p")
    p2 = p1.find_next_sibling("p")
    content["contents"]["Inicio: "] = [p1.get_text()]


    for item in soup.find_all(class_="lwptoc_item"):
        a = item.find("a")
        a = a["href"][1:]
        ids.append(a)
        labels.append(item.find(class_="lwptoc_item_label").get_text())

    inicialP = soup.find(id=ids[0])
    secondP = inicialP.parent.find_next_siblings(["p", "ul"])
    if p2 not in secondP:
        content["contents"]["Inicio: "].append(p2.get_text())

    for i in range(len(ids)):
        first = soup.find(id=ids[i])
        if i != len(ids) - 1:
            second = soup.find(id=ids[i + 1])
            parent1 = first.parent
            parent2 = second.parent.find_next_siblings(["p", "ul"])
            inverted = False
            if labels[i] in content["contents"].keys():
                content["contents"][labels[i] + " Invertido"] = []
                inverted = True
            else:
                content["contents"][labels[i]] = []
            for tag in parent1.find_next_siblings(["p", "ul"]):
                if tag not in parent2:
                    if inverted:
                        content["contents"][labels[i] + " Invertido"].append(tag.get_text())
                    else:
                        content["contents"][labels[i]].append(tag.get_text())
    
    return content


def get_card_urls(url):
    info = {}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    for item in soup.find_all("h2"):
        a = item.find("a")
        if a:
            info[a.get_text().replace("/", "ou")] = a["href"]

    return info


#major = get_card_urls("https://tarotfarm.com.br/arcanos-maiores-tarot/")
#cups = get_card_urls("https://tarotfarm.com.br/naipe-de-copas-significados/")
#swords = get_card_urls("https://tarotfarm.com.br/naipe-de-espadas-significados/")
pentacles = get_card_urls("https://tarotfarm.com.br/naipe-de-ouros-significados/")
wands = get_card_urls("https://tarotfarm.com.br/naipe-de-paus-significados/")

all_cards = {"pentacles": pentacles, "wands": wands}


for arcana in all_cards.keys():
    with open(arcana + ".json", "w", encoding='utf-8') as outfile:
        json.dump(all_cards[arcana], outfile, ensure_ascii=False)
    for card in all_cards[arcana].keys():
        data = get_card_content(card, all_cards[arcana][card])
        with open(card + ".json", "w", encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)
