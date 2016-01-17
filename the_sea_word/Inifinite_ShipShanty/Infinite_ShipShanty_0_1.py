# here we go. This is a thing to scrape earthquake data from the net.
import os
from bs4 import BeautifulSoup  # URL parser
import urllib2  # allows python to get things from URLs
from time import sleep
import random

# fetch raw html
page = urllib2.urlopen("http://www.metoffice.gov.uk/public/data/CoreProductCache/ShippingForecast/Latest/")
directory = '/home/smc/Downloads/shanties/'

delay = input('time delay: ')

# convert page into a recognised set of DOM projects, run for a dump of the page
# soup = BeautifulSoup(page, "html.parser")

soup = BeautifulSoup(page.read())

report = soup.find_all('report')

def getFilesInFolder(directory, extension):
    fileList = []
    for file in os.listdir(directory):
            if file.endswith(extension):
                    fileList.append(file)
    return fileList

fulldir = directory+random.choice(getFilesInFolder(directory, '.txt'))

shantylines = []

with open(fulldir) as infile:
    shantylines = [line.strip() for line in infile]


# print fulldir
# print shantylines

shippingarray = []

statearray = ['wind', 'main', 'seastate', 'visibility', 'all']

for thing in report:
    forecast = thing.find_all('area-forecasts')
    for item in forecast:
        area = item.find_all(random.choice(statearray))
        for thingy in area:
            i = 0
            shippingarray.append(thingy.get_text())

# print shippingarray

i = 0
num = 0

while True:
    if i < 3:
        print shantylines[num%len(shantylines)]
        num = num + 1
        i = i + 1
        sleep(delay)
    else:
        print random.choice(shippingarray)
        i = 0
        sleep(delay)
