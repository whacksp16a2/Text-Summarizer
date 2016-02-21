from bs4 import BeautifulSoup
import urllib2, sys, re
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def wiki_summary(title):
    title = title.replace(" ", "_")
    title = title.strip(" ").title()
    if title == "The_Alchemist":
        site = "http://en.wikipedia.com/wiki/The_Alchemist_(novel)"
    else:
        site = "http://en.wikipedia.com/wiki/" + title

    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site,headers=hdr)
    page = urllib2.urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')
    plot_location_1 = str(soup.find(id="Plot"))
    plot_location_2 = str(soup.find(id="Plot_summary"))
    plot_location_3 = str(soup.find(id="Synopsis"))
    plot_location_4 = str(soup.find(id="Summary"))

    body = str(soup.body)
    if plot_location_1 in body:
    	index = body.index(plot_location_1)
    elif plot_location_2 in body:
    	index = body.index(plot_location_2)
    elif plot_location_3 in body:
    	index = body.index(plot_location_3)
    elif plot_location_4 in body:
    	index = body.index(plot_location_4)
    else:
    	return ""

    plot_loc = body[index:]
    index_para_start = plot_loc.index("<p>")
    index_para_end = plot_loc.index("<h2>")

    unstripped = str(plot_loc[index_para_start:index_para_end])

    stripped = stripHTMLTags(unstripped)
    return stripBrackets(stripped)

def stripHTMLTags(html):
    html = re.sub(r'<{1}br{1}>', '\n', html)
    s = MLStripper()
    s.feed(html)
    text = s.get_data()
    if "External links" in text:
        text, sep, tail = text.partition('External links')
    if "External Links" in text:
        text, sep, tail = text.partition('External Links')
    text = text = text.replace("See also","\n\n See Also - \n")
    text = text.replace("*","- ")
    text = text.replace(".", ". ")
    text = text.replace("  "," ")
    text = text.replace("""   /
        / """, "")
    return text

def stripBrackets(text):
    for i in range(100):
        text = text.replace("[" + str(i) + "]","")
    return text



if __name__ == "__main__":
    book_title = str(raw_input("What's your favorite book?"))
    print(wiki_summary(book_title))
