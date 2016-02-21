from urllib import urlopen
from bs4 import BeautifulSoup
from summarizer import getSummaryFromWebsite
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getSearchableTitle(bookTitle):
    return bookTitle.replace(" ", "+")

def getFirstHyperlinkText(searchResults, divisionNumber):
    # divisionNumber dictates which subdivision of the URL we want
    for result in searchResults:
        hrefText = result.a['href']
        bookTitleFromURL = hrefText.split('/')[divisionNumber]
        print(hrefText)
        print(len(hrefText.split('/')))
        if bookTitleFromURL.lower() in bookTitle.lower() and bookTitleFromURL.lower() is not "":
            return bookTitleFromURL.lower()


def getShortenedName(bookTitle):
    """Get the name that sparknote refers to the book as"""
    searchableTitle = getSearchableTitle(bookTitle)
    search_url = "http://www.sparknotes.com/search?q={0}".format(searchableTitle)
    html = urlopen(search_url)
    bsObj = BeautifulSoup(html.read())

    searchResults = bsObj.findAll("div", {"class": "search-result"})
    hyperlinkText = getFirstHyperlinkText(searchResults, 4)
    return hyperlinkText
    """for result in searchResults:
        hrefText = result.a['href']
        bookTitleFromURL = hrefText.split('/')[3]
        if bookTitleFromURL.lower() in bookTitle.lower() and bookTitleFromURL.lower() is not "":
            return bookTitleFromURL.lower()"""


def getSparknoteURL(bookTitle):
    shortenedName = getShortenedName(bookTitle)
    if (getShortenedName(bookTitle) is ""):
        shortenedName = getShortenedName(bookTitle.replace(" ", "-"))
    url = "http://www.sparknotes.com/lit/{0}/summary.html".format(shortenedName)
    return url


def getSummary(bookTitle, sentences_count):
    url = getSparknoteURL(bookTitle)
    return getSummaryFromWebsite(url, sentences_count)


if __name__ == "__main__":
    bookTitle = str(raw_input("What's your favorite book?"))
    sentences_count = 2
    sentences = getSummary(bookTitle, sentences_count)
    print(sentences).encode(sys.stdout.encoding, errors='replace')

