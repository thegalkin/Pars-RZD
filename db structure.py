from bs4 import BeautifulSoup as bs
import sys, time, re
import pathlib as ph
from os import listdir,chdir
from os.path import isfile, join
def appendToDb():
    return


chdir("{}/downloads".format(ph.Path.cwd()))
onlyfiles = [f for f in listdir(ph.Path.cwd()) if isfile(join(ph.Path.cwd(), f))] # создаем список файлов в папке загрузок
i = 0
items = []
for fName in onlyfiles:
    i+=1
    if i == 2: break
    with open(str(join(ph.Path.cwd(), fName)), "r") as site:
        soup = bs(site.read(), "lxml")
        for line in soup:
            item = soup.find("td", class_="availabiItm").text
            item = re.sub("^\s+|\n|\t|\s+$", '', item)
            items.append(item)


print(items)