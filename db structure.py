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
for fName in onlyfiles:
    i+=1
    if i == 2: break
    with open(str(join(ph.Path.cwd(), fName)), "r") as site:
        print(bs(site.read(), "lxml").prettify())
