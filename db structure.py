from bs4 import BeautifulSoup as bs
import sys, time, re
import pathlib as ph
from os import listdir,chdir
from os.path import isfile, join
import openpyxl as opx
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
        """for line in soup:
            item = soup.find("td", class_="availabiItm").text
            item = re.sub("^\s+|\n|\t|\s+$", '', item)
            items.append(item)"""
        print(soup.title.string)
        for tag in soup.findAll("td", class_="availabiItm"):
            
            print("{0}: {1}: ".format(tag.name, re.sub("\n|\t", '', tag.h3.string) ))


            """ print("коляска :", end="")
            if tag.find(class_="pass-ico ico-color1"):
                print("25%")
            elif(tag.find(class_="pass-ico ico-color2") ):
                print("12.5%")
            elif tag.find(class_="pass-ico ico-color3") :
                print("0%")"""
        print("Коляска: ")
        for tag in soup.findAll("td", class_="icoLineType1"):
            
            if tag.find(class_="pass-ico ico-color2"):
                print("25%")
            elif(tag.find(class_="pass-ico ico-color1") ):
                print("12.5%")
            elif tag.find(class_="pass-ico ico-color0") :
                print("0%")
        print("Трость: ")
        for tag in soup.findAll("td", class_="icoLineType2"):
            
            if tag.find(class_="pass-ico ico-color2"):
                print("25%")
            elif(tag.find(class_="pass-ico ico-color1") ):
                print("12.5%")
            elif tag.find(class_="pass-ico ico-color0") :
                print("0%")
        print("Слух: " )
        for tag in soup.findAll("td", class_="icoLineType3"):
            
            if tag.find(class_="pass-ico ico-color2"):
                print("25%")
            elif(tag.find(class_="pass-ico ico-color1") ):
                print("12.5%")
            elif tag.find(class_="pass-ico ico-color0") :
                print("0%")
        print("Зрение: " )
        for tag in soup.findAll("td", class_="icoLineType4"):
            
            if tag.find(class_="pass-ico ico-color2"):
                print("25%")
            elif(tag.find(class_="pass-ico ico-color1") ):
                print("12.5%")
            elif tag.find(class_="pass-ico ico-color0") :
                print("0%")
        
        wb = opx.Workbook()
        ws = wb.active()
        ws.title = soup.title.string
        
