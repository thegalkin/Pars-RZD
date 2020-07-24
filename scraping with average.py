# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup as bs
import sys, time, re
import pathlib as ph
from os import listdir,chdir
from os.path import isfile, join
import openpyxl as opx
def appendToDb():
    return

homeDirectory = ph.Path.cwd()
chdir("{}/downloads".format(ph.Path.cwd()))
onlyfiles = [f for f in listdir(ph.Path.cwd()) if isfile(join(ph.Path.cwd(), f))] # создаем список файлов в папке загрузок

i = 0
items = []
#print(onlyfiles)
for fName in onlyfiles:
    
    i+=1
    #if i == 2: break
    with open(str(join(ph.Path.cwd(), fName)), "r") as site:
        try:
            soup = bs(site.read(), "lxml")
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
       
        
        #services and summing
        summing = []
        services = []
        
        for tag in soup.findAll("td", class_="availabiItm"):
            try:
                services.append(re.sub("\n|\t", '', tag.h3.string))
            except AttributeError:
                re.sub("\n|\t", '', tag.string)
            if tag.find(class_="percentRate pR-1"):
                summing.append(tag.find(class_="percentRate pR-1").string.replace(".", ",") )
            elif(tag.find(class_="percentRate pR-2") ):
                summing.append(tag.find(class_="percentRate pR-2").string.replace(".", ",") )
            elif tag.find(class_="percentRate pR-3") :
                summing.append(tag.find(class_="percentRate pR-3").string.replace(".", ",") )
        
        

        print(fName.replace(".html", ""))
        wb = opx.Workbook()
        ws = wb.active
        try: 
            ws.title = soup.title.string
        except ValueError:
            print("ValueError")
            pass
       
        
        ws.append(tuple(fName.replace(".html", "")))
        for row in zip(services, wheelChair, walkStick, hearing, seeing, summing):
            ws.append(row)
        chdir("{}/tables".format(homeDirectory))
        wb.save('{}.xlsx'.format(fName.replace(".html", "")))
        wb.close()
        chdir("{}/downloads".format(homeDirectory))

    print("{}%".format(i/len(onlyfiles)*100))
    