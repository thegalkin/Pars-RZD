from urllib.request import urlopen
import time, bs4
def downloadPage(link):
    html = urlopen(link).read().decode('utf-8')
