import urllib.request, urllib.error, random, sqlite3
from bs4 import BeautifulSoup
import re
#possible sources
quote_pages = ["https://www.thelatinlibrary.com/tibullus1.html", "https://www.thelatinlibrary.com/tibullus2.html", "https://www.thelatinlibrary.com/tibullus3.html"]

def main():


	#open a random book of Tibullus
	book = random.randint(0, len(quote_pages) - 1)
	page = urllib.request.urlopen(quote_pages[book])
	soup = BeautifulSoup(page, 'html.parser')

	#select a random valid (i.e. not the title) passage of Tibullus
	numPars = len(soup.find_all('p'))
	par = random.randint(0, numPars-1)
	#passage = soup.select('p')[par].get_text(strip=True)
	passage = soup.select('p')[par].get_text(separator=" ", strip=True).rstrip("\n")
	while(not len(passage)>50):
		par = random.randint(0, numPars-1)
		passage = soup.select('p')[par].get_text(strip=True)
	


	#parse paragraph into sentences (approx.)
	ends = re.compile('[.!?]')
	sents = ends.split(passage)
	#print(passage)
	#select random sentence
	while("" in sents):
		sents.remove("")
	sen_indx = random.randint(0, len(sents)-1)
	sen = sents[sen_indx].lower()
	digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	for n in digits:
		num = "" + str(n)
		while num in sen:
			sen.replace(num, '')
	print(sen)



if __name__ == '__main__':
	main()