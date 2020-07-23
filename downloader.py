import requests as re
from bs4 import BeautifulSoup as bs
import time
import pathlib as ph
headers  = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4', 'Cache-Control': 'max-age=0', 'Connection': 'close', 'Host': 'www.propertyguru.com.sg', 'Referer': 'propertyguru.com.sg/singapore-property-listing/…', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
def downloadPage(link):
    html = re.get(url=url, headers=headers)
    html = bs(html, "html")
    name = html.title()
    with open("{}.html".format(name), "w+") as f:
        f.write(html)

def listImporter():
    linksFile = open("вокзалы.xlsx", "r")
    return linksFile

ph.Path.
linksFile = listImporter()







