
import httplib2
import urllib2
import re
import string
import os
import time
from bs4 import BeautifulSoup, SoupStrainer
import unicodedata

def isWordInLine(line, word):
	
	exclude = set(string.punctuation)
	#get rid of the punctuation
	line = ''.join(ch for ch in line if ch not in exclude)
	#explode the line by the spaces
	words = line.split(" ")
	#go through the list of words
	for aword in words:
		#if we fget a match return true
		if aword==word and len(word)>4:
			#print "MATCHING WORD IS ",word
			return True
	#if we get here then we havn't found one so return false
	return False


# def doesShantyContainMatch(filename, word):
# 	#load the shanty file
# 	file_object = open(filename, 'r')
# 	text = file_object.read()
# 	#go through all the lines (split by carriage return)
# 	lines = text.split('\n')
# 	for line in lines:

# 		if isWordInLine(line, word):
# 			#if we get a match return true
# 			return True
# 	#otherwise return false
# 	return False

def swapInLine(metline, filename):
	file_object = open(filename, 'r')
	text = file_object.read()
	#go through all the lines (split by carriage return)
	lines = text.split('\n')
	#print lines
	#keep a list of the lines so far
	newlines = []
	#for each line either swap in a new line or leave it as it is
	textChanged = False
	for shantyline in lines:
		#print shantyline
		containsWord = False
		for word in metline.split(" "):
			if isWordInLine(shantyline, word):
				containsWord = True
		if containsWord:
			newlines.append(metline)
			textChanged = True
		else:
			###print "appnding"
			newlines.append(shantyline)

	newShantyText = ""
	for aline in newlines:
		newShantyText+=aline
		newShantyText+="\n"


	#print "NEW SHANTY",newShantyText
	file_object.close()
	#time.sleep(1)

	if textChanged:
		print "CHANGED ",filename
		target = open(filename, 'w')
		target.write(newShantyText)
		target.close()

	#otherwise return false
	return newlines

	#html = urllib.urlopen('http://www.nytimes.com/2009/12/21/us/21storm.html').read()

url = "http://www.metoffice.gov.uk/public/data/CoreProductCache/ShippingForecast/Latest/"

page = urllib2.urlopen(url)
			#make the soup
soup = BeautifulSoup(page.read())

#print soup
report =  soup.find_all('report')


#workign bit




# write a function to get all files within a folder

directory = '/Users/tomschofieldart/Desktop/PYTHON/shanties'


def getFilesInFolder(directory, extension):
    fileList = []
    for file in os.listdir(directory):
            if file.endswith(extension):
                    fileList.append(file)
    return fileList

 

filelist = getFilesInFolder(directory, '.txt')

#for all the things in the shipping forecast
for thing in report:
	#go through all the foredasets
	forecasts = thing.find_all('area-forecasts')
	
	for forecast in forecasts:
		
		winds = forecast.find_all('wind')
		for wind in winds:
			for afile in filelist:
				#print 'trying file ', afile
				newshanty = swapInLine(wind.get_text(), directory+"/"+afile)
