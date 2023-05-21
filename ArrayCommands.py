import re
from urllib.parse import urlparse
from collections import Counter

def count(warays):
    ## WebArray goes from youtube youtube google google google ---> google:3 , youtube:2
    print(warays)
    print(Counter(warays))
    nwear = Counter(warays)
    return nwear.most_common()


def findNames(ProssesedArray):
    ## creates WebArray wich has the names of websites, such as youtube.com or google.com
    WebArray = []
    thingURL = ""
    for thingURL in ProssesedArray:
        WebArray.append(urlparse(thingURL.rstrip(r'",').strip(r'"url": "')).netloc)
    print(WebArray)
    war = WebArray
    return war

def exportWebArray(expArray):
    with open("Export.txt", "+w") as acfile:
        for thingth in expArray:
            acfile.write(str(thingth[0]) + " " + str(thingth[1]) + "\n")
    print(expArray)

def cleanWebArray(saveExpression, waray):
    i = 0
    for urlth in waray:
        waray[i] = re.search(saveExpression, urlth)
        i = i + 1

    print(waray)