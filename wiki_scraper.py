# install beautifulsoup
# sudo apt-get install python3-bs4

from bs4 import BeautifulSoup
import urllib2, sys
#from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://en.wikipedia.com/wiki/Robinson_Crusoe")
bsObj = BeautifulSoup(page.read())
print bsObj
