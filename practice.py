import urllib.request as urllib
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re

HOST = "https://phenocam.sr.unh.edu"
SITE = "/webcam/browse/arsmorris2/2017/07/13/"

req = urllib.urlopen(HOST + SITE)

soup = BeautifulSoup(req)

siteinfo = soup.findAll("div", {"id": "siteinfo"})

numImages = siteinfo[0].find(text=re.compile(r'Number of Images: (.*)'))


if("Number of Images: 0" in str(numImages)):
    print("it matches")
