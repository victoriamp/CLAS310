import urllib.request, urllib.error
import random
import sqlite3
from bs4 import BeautifulSoup

#possible sources
quote_pages = ["https://www.thelatinlibrary.com/tibullus1.html", "https://www.thelatinlibrary.com/tibullus2.html", "https://www.thelatinlibrary.com/tibullus3.html"]


def main():
	#open a random book of Tibullus
	book = random.randint(0, len(quote_pages) - 1)
	page = urllib.request.urlopen(quote_pages[book])
	soup = BeautifulSoup(page, 'html.parser')

	#select a random valid (i.e. not the title) paragraph of Tibullus
	numPars = len(soup.find_all('p'))
	par = random.randint(0, numPars-1)
	passage = soup.select('p')[par].get_text(strip=True)
	while(not len(passage)>50):
		par = random.randint(0, numPars-1)
		passage = soup.select('p')[par].get_text(strip=True)
	
	#parse paragraph into small passages


	#select random passage



if __name__ == '__main__':
	main()