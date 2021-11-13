''' Scraping in (http://py4e-data.dr-chuck.net/comments_1003519.html) this
URL and find the sum of no. in this web page. '''


import urllib.request, urllib.parse, urllib.error #imported for getting on web(socket or connection)
from bs4 import BeautifulSoup   #for reading html on web page
y = 0
url = input("Enter url- ") #http://py4e-data.dr-chuck.net/comments_1003519.html
html = urllib.request.urlopen(url).read()
print(html) 

soup = BeautifulSoup(html,"html.parser") # to make htlm organised and read-able 
print(soup)

tags = soup("span") # makes seperate list of this specific tag with data we want
print(tags)

for tag in tags :
    z = tag
    for x in z :
        y = y + int(x)
print(y)
        
        



# to make dictionary of words with with counting(which name comes how many times)
'''d = dict()
tags = soup("tr")
for tag in tags :
    q = tag.contents[0]
    for k in q :
        d[k] = d.get(k,0) + 1
print(d)'''   
    
