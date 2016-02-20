from urllib import urlopen
from bs4 import BeautifulSoup
from summarizer import getSummaryFromWebsite


def getSearchableTitle(bookTitle):
    return bookTitle.replace(" ", "+")


def getShortenedName(bookTitle):
    """Get the name that sparknote refers to the book as"""
    searchableTitle = getSearchableTitle(bookTitle)
    search_url = "http://www.sparknotes.com/search?q={0}".format(searchableTitle)
    html = urlopen(search_url)
    bsObj = BeautifulSoup(html.read())

    searchResults = bsObj.findAll("div", {"class": "search-result"})
    for result in searchResults:
        hrefText = result.a['href']
        bookTitleFromURL = hrefText.split('/')[4]
        #print(bookTitleFromURL)
        if bookTitleFromURL.lower() in bookTitle.lower() and bookTitleFromURL.lower() is not "":
            #print bookTitleFromURL.lower()
            return bookTitleFromURL.lower()


def getSparknoteURL(bookTitle):
    shortenedName = getShortenedName(bookTitle)
    url = "http://www.sparknotes.com/lit/{0}/summary.html".format(shortenedName)
    return url


def getSummary(bookTitle, sentences_count):
    url = getSparknoteURL(bookTitle)
    return getSummaryFromWebsite(url, sentences_count)


if __name__ == "__main__":
    bookTitle = "Absalom Absalom"
    sentences_count = 2
    sentences = getSummary(bookTitle, sentences_count)
    for sentence in sentences: print(sentence)
