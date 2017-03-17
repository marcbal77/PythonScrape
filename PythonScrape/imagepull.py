#!/usr/bin/python

#from pulls for url and beautysoup imports include non-false positives
from bs4 import BeautifulSoup
from urllib2 import urlopen

#richmond
site = "http://richmond.craigslist.org/rea/"
table = BeautifulSoup(urlopen(site))
items = table('p')
linkdict = {}
i = 0

#for in loop
for item in items[:-1]:
    i=i+1
    itempostlink = item('a')[0]['href']
    itemlink = site[:-5] + itempostlink
    linkdict[i] = itemlink

#for a side project, include decible levels
#incorporate print out for Beautiful Soup
for i, link in linkdict.iteritems():
    #Print available insert for linkdict
    print i, linkdict[i]
    images = BeautifulSoup(urlopen(linkdict[i]))('img')
    imagecounter = 0
    #image for loop
    for image in images:
        imagecounter +=1
        image_url =image['src']
        print image_url
        image = urlopen(image_url)
        local = open("c:\\temp\\"+str(i)+"."+str(imagecounter)+".jpg",'wb')
        local.write(image.read())
        local.close()
    print
