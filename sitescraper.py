import urllib.request as urllib
import urllib.error as urlliberror
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re
import os

#HOST = reference envrionment var here


def main():
        file = open("./sitesrevised", "r")
        sitelist = []
        for line in file.readlines():
                print(line)
                for site in line.split(','):
                        sitelist.append(site[2:len(site)-3])
                

        # print("\n", sitelist)
        for site in sitelist:
                # print(HOST + site)
                req = urllib.urlopen(HOST + site)
                parseImageURLs(req, site)

# with urllib.request.urlopen(req) as response:
#    the_page = response.read()

imageUrlList = []

def numDays(month):
        # print(month)
        if(month in '02'):
               return 28
        
        elif(month in ['01', '03', '05', '07', '08', '10', '12']):
                return 31
        else:
                return 30

def parseImageURLs(req, site):
        soup = BeautifulSoup(req)
        yearsummary = soup.findAll("div", {"class": "yearsummary"})
        # print(len(yearsummary))
        if(len(yearsummary)<2):
                return
        anchorTags = yearsummary[1].findAll("a")
        # print(anchorTags)

        months = []

        for i in anchorTags:
        # print(i)
                i = str(i)
                if(site in i):
                        urlMonths = re.search("href=(\".*\")", i)
                        # print(urlMonths.group(0))
                        months.append(urlMonths.group(0))


        urlSubString = []
        intMonths = []

        for i in months:
                # print("i", i)
                subString = re.search("(\".*)", i)
                # print(subString.group(0))
                urlSubString.append(subString.group(0))
        months = []

        print('urlSubString', urlSubString)
        iterUrlSubString = iter(urlSubString)
        urlSubString = []
        print('iterUrlSubString', iterUrlSubString)
        next(iterUrlSubString)
        for i in iterUrlSubString:
                intMonths.append((i[len(i) - 4:len(i)-2], i))

        # print("intMonths", intMonths)
        # print(anchorTags[0]['name'])
        year_month_day_url = []
        url = ''

        for i in intMonths:
                stringday = ''
                Days = numDays(i[0])
                for j in range(1, Days+1):
                        if j < 10:
                                stringday = "0"+str(j)
                        else:
                                stringday = str(j)
                        
                        url = i[1].strip('\"')
                        url += stringday
                        year_month_day_url.append(url)
        intMonths = []
        # print(url)
        # print(year_month_day_url)

        for date in year_month_day_url:
                urlToReq = HOST+date
                try:
                        req = urllib.urlopen(urlToReq)
                except urlliberror.HTTPError as e:
                        print("HTTPError is: {}".format(e.code))
                        continue
                except urlliberror.URLError as e:
                        print('URLError: {}'.format(e.reason))
                        continue
                soup = BeautifulSoup(req, "html5lib")
                siteinfo = soup.findAll("div", {"id": "siteinfo"})
                numImagesTag = siteinfo[0].find(text=re.compile(r'Number of Images: (.*)'))
                if("Number of Images: 0" in str(numImagesTag)):
                        continue
                else:
                        sitename = date.split('/')[3]
                        retrieveImageUrls(soup, sitename)
                # print(soup)



def retrieveImageUrls(soup, sitename):
        daysummary = soup.find('div', {'id': "daysummary"})
        # print(daysummary)
        table_body = daysummary.find('tbody')
        # print(table_body)
        rows = table_body.find_all('tr')
        imageUrlList = []
        for row in rows:
                cols = row.find_all('td')
                for col in cols:
                        a = col.find('a')
                        imageurl = a['href']
                        # imageTimeStamp = col.find('span').getText()
                        imageUrlList.append(HOST+imageurl)
                       
        # print("\n\n", imageUrlList)

        storelist(imageUrlList, sitename)
        imageUrlList = []

def storelist(imageUrlList, sitename):
        f = open('./images/'+ sitename+'.txt',"a+")
        for item in imageUrlList:
                f.write(item+'\n')
        f.close()

if (__name__ == "__main__"):
        main()





# print("title ", soup.title)

# links = soup.find_all('img')

# print(links)




