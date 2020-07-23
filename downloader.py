import requests as requests
from bs4 import BeautifulSoup as bs
import time
import pathlib as ph
from os import chdir

headers  = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4', 'Cache-Control': 'max-age=0', 'Connection': 'close', 'Host': 'www.propertyguru.com.sg', 'Referer': 'propertyguru.com.sg/singapore-property-listing/…', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
def downloadPage(url):
    html = requests.get(url=url)
    html = str(html)
    html = html.decode("WINDOWS-1251").encode("utf-8")
    html = bs(html.text, "html")
    html = str()
    name = str(html.title())
    #name = name[name.find("Вокзал ")+1:]
    with open("{}.html".format(name), "w+") as f:
        f.write(html)


linksFile = open("terminals.txt", "r")


chdir("{}/downloads".format(ph.Path.cwd()))
i = 0
#print("{} - тута".format(linksFile[:linksFile.find("\n")]))
for link in linksFile:
    i+=1
    if i == 4: break
    time.sleep(1)
    downloadPage(link)
    print("{} - идет".format(i))









