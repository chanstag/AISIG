#! /usr/bin/python3

import urllib.request as urllib
from html.parser import HTMLParser
from bs4 import BeautifulSoup

#HOST = reference environ var
def main():
    with open('./sitesrevised', 'r') as file:
        browseList = file.read().split(',').trim('\n')

        for site in browseList:
            req = urllib.urlopen(HOST + site)
            soup = BeautifulSoup(req)
            yearsummary. = soup.findAll("div", {"class": "yearsummary"})
            anchorTags = yearsummary.findChildren("a")
            print()
