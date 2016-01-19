# =====================INFINITE SHIPPING SHANTY=======================
# to use this, you will need to use Tom Schofield's Sea Shanty Scraper
# to gather a collection of shanties from the net in plain text.
# You'll then need to point this script to the correct directory.
# This script scrapes shipping forecast data from the Met Office API
# and creates an infinite mashup. This application is designed to run
# in the terminal.

# 'delay' is the amount of time between lines.
# 'reset' is the number of lines before a new shanty is loaded and
# the shipiing forecast is re-scraped.

# created for Hack The Marine, 16th January 2015


import os
from bs4 import BeautifulSoup  # URL parser
import urllib2  # allows python to get things from URLs
from time import sleep
import random


delay = input('time delay: ')
reset = input('reset interval: ')

# load scraped sea shanties
directory = '/path/to/sea/shanties/'


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

num = 0

while True:

    if num == 0:
        # fetch raw html
        page = urllib2.urlopen("http://www.metoffice.gov.uk/public/data/CoreProductCache/ShippingForecast/Latest/")

        # convert page into a recognised set of DOM projects, run for a dump of the page
        # soup = BeautifulSoup(page, "html.parser")

        soup = BeautifulSoup(page.read())

        report = soup.find_all('report')

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
        num = num + 1

    elif num < reset:

        if i < 3:
            print shantylines[num % len(shantylines)]
            num = num + 1
            i = i + 1
            sleep(delay)
            num = num + 1
        else:
            print random.choice(shippingarray)
            i = 0
            num = num + 1
            sleep(delay)

    elif num >= reset:
        num = 0
