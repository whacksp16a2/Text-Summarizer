from bs4 import BeautifulSoup
import urllib2, sys, re
from HTMLParser import HTMLParser

book_title = str(raw_input("What's your favorite book?"))


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
	site = "http://en.wikipedia.com/wiki/" + title
	print site

	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(site,headers=hdr)
	page = urllib2.urlopen(req)


	#title = "The Book Thief"
	soup = BeautifulSoup(page, 'html.parser')
	plot_location_1 = str(soup.find(id="Plot"))
	plot_location_2 = str(soup.find(id="Plot_summary"))

	body = str(soup.body)
	plot = "Plot"
	if plot_location_1 in body:
		index = body.index(plot_location_1)
	else:
		index = body.index(plot_location_2)

	
	plot_loc = body[index:]
	index_para_start = plot_loc.index("<p>")
	index_para_end = plot_loc.index("<h2>")

	unstripped = str(plot_loc[index_para_start:index_para_end])
	
	print unstripped
	return unstripped 
	# stripped = unstripped.split("<p>")


	# more_stripped = []
	# for i in range (len(stripped)):
	# 	if "</p>" in stripped[i]:
	# 		more_stripped.append(stripped[i])

	# print ''.join(more_stripped)

	# return ''.join(more_stripped)


	
	

	#more_stripped = ''.join(more_stripped).split("</p>")

	# moree_stripped = []
	# for x in range (len(more_stripped)):
	# 	if "</p>" in more_stripped[x]:
	# 		moree_stripped.append(more_stripped[x])
	# print more_stripped


	# almost_final_strip = more_stripped[0::2]


	# print almost_final_strip		


	# def paragrapher(big_string, start, end):
	# 	if len(big_string) > 1:
	# 		para_start = "<p>"
	# 		para_end = "</p>"
	# 		index_para_start = unstripped.index(para_start)
	# 		index_para_end = unstripped.index(para_end)
	# 		new_string = big_string[index_para_start:index_para_end]
	# 		recursion = paragrapher(new_string)
	# 	else:
	# 		return True
	# 	return big_string[start:end] + recursion

	# 	#stripped = unstripped.strip('<p>')
	# 	# print stripped 


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
	 / ""","")
	    return text

final = stripHTMLTags(wiki_summary(book_title))
for i in range (50):
	final = final.replace("[" + str(i) + "]","");

print final