from bs4 import BeautifulSoup as bs
import json
import requests


def saveJson(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def fetchHtmlAndParse(url):
    html = requests.get(url, headers={'User-Agent': '*/*'})
    return bs(html.content, 'html.parser')


def removeUnicode(text):
    return text.encode('ascii', 'ignore').decode().replace('\"', '')



def fetchLinks(url, element, className):
    bsObj = fetchHtmlAndParse(url)
    links = []

    for link in bsObj.find_all(element, class_=className):
        if(link.a != None):
            links.append(link.a.get('href'))

    return links


def fetchMenuLinks(url, element, className):
    bsObj = fetchHtmlAndParse(url)
    links = []

    list = bsObj.find(element, class_=className)

    for item in list.find_all('li'):
        if(item.a != None):
            links.append(item.a.get('href'))

    return links