from bs4 import BeautifulSoup
import urllib2, sys

book_title = str(raw_input("What's your favorite book?"))




def wiki_summary(title):
	title = title.replace(" ", "_")
	title = title.strip(" ").title()
	site = "http://en.wikipedia.com/wiki/" + title
	print site

	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(site,headers=hdr)
	page = urllib2.urlopen(req)


	title = "The Book Thief"
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

	return unstripped

	para_start = 
	para_end = 

		#stripped = unstripped.strip('<p>')
		# print stripped 

print wiki_summary(book_title)