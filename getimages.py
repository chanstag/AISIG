from os import listdir, makedirs
from os.path import isfile, join, splitext
import errno
import urllib.request as urllib
import urllib.error as urlliberror

mypath = "/home/chanstag/ACM/AI/images/"

def readOSFiles():
    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print(onlyfiles)
    pullimages(onlyfiles)

def pullimages(onlyfiles):
    for txtfile in onlyfiles:
        print(txtfile)
        file = open('./images/'+txtfile, 'r')
        foldername = splitext('./images/'+txtfile)[0]
        foldername = foldername.split('/')[-1]
        print("foldername", foldername)
        print(mypath+foldername)
        try:
            makedirs("./images/"+foldername+"/training")
            makedirs("./images/"+foldername + "/testing")
            makedirs("./images/"+foldername + "/validation")
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        # directory = mypath+foldername
        i = 0
        numimages = 0
        for imageurl in file.readlines():
            imagename = imageurl.split('/')[-1]
            print("imagename", imagename)
            if( i % 3 == 0):
                storagelocation = "./images/"+foldername+"/training/"+imagename
                urllib.urlretrieve(imageurl, storagelocation.strip('\n'))
            elif(i % 3 == 1):
                storagelocation = "./images/"+foldername+"/testing/"+imagename
                urllib.urlretrieve(imageurl, storagelocation.strip('\n'))
            else:
                storagelocation = "./images/"+foldername+"/validation/"+imagename
                urllib.urlretrieve(imageurl, storagelocation.strip('\n'))
            if(numimages == 99):
                break
            i += 1
            numimages += 1


readOSFiles()