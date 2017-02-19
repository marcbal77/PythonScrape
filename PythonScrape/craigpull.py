#!/usr/bin/python
from BeautifulSoup import BeautifulSoup   
from urllib2 import urlopen               

# site pull
site = "http://sfbay.craigslist.org/rea/" 
html = urlopen(site)                      
soup = BeautifulSoup(html)                
postings = soup('p')                      

# for loop
for post in postings:                     
    print post('a')[0].contents[0]        
    print post('a')[0]['href']     
Contact GitHub API Training Shop Blog About
