# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error  #or instead of importing libraries we can do as in assingment 12
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')         #use https:// before entering url
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')  #Beautiful Soup is a Python package for parsing HTML and XML documents
print(soup)

#(including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for
#parsed pages that can be used to extract data from HTML, which is useful for web scraping.

                             # Retrieve all of the anchor tags
tags = soup('a')             # all links and text for links 
for tag in tags:
    print(tag.get('href', None))  #get href (which is attribute of "a") (i.e. links destination) or nothing



# this code to print all links heads in front of us when we open an url or web page
