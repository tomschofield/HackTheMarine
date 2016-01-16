
import httplib2
import urllib2
import re
from bs4 import BeautifulSoup, SoupStrainer
import unicodedata



#iterate through all the links om the page and find one that matches the pattern we want
def getLinksToSongs(master_url):
	http = httplib2.Http()
	status, response = http.request(master_url)
	for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
		if link.has_attr('href'):
			_url = link['href']
			#http://www.eufeeds.eu/at
			exploded = _url.split("/")
			if len(exploded)>2:
				#ignore the internal links
				#print exploded[2]
				if exploded[2]=='www.arrr.net':
					#print 'gotcha'
					try:
						site_text = getShanty(_url)
						print "////////////////////////////////////////// GETTING TEXT FROM ", _url, "//////////////////////////////////////////"
						print site_text
					except:
						print "UNPARSEABLE LINK"
				
			
			
	pass



def getShanty(url):
	
			#read the page
	page = urllib2.urlopen(url)
			#make the soup
	soup = BeautifulSoup(page.read())
	#grab the lyrics div
	song = soup.find(id="lyrics").get_text()
	#banner contains the title in an h2 tag inside it
	div = soup.find(id="banner")
	title = div.h2.text #find_all('h2').text

	exploded = title.split("/")
	fname = exploded[0]
	string_song = song.encode('ascii','ignore')
	try:
		print type(string_song)
	except Error:
		print Error
	
	#check it\s not nonsense
	if(len(string_song)>10):
		fname+=".txt"
		target = open(fname, 'w')
		target.write(string_song)
		target.close()

	return "ok"


getLinksToSongs('http://www.arrr.net/shanties/')


#get body