# WebCrawl
# by TeeJ
# 01-26-2019

# Goal: The purpose of this program is to exploit the internet by grabbing data.
# I aim to run this throughout the day on my Raspberry Pi and collect pricing
# data on items that I am interested in. For fun.

# import packages
from bs4 import BeautifulSoup
import requests
import re

# establish variables
# site = "http://www.example.com"
# site = "https://www.amazon.com"
# site = "https://www.pandora.com"

# simple example


# boss battle 
site = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search--alias%3Daps&field-keywords=Data+Science&rh=i%3Aaps%2Ck%3AData+Science"

# extract data from the site
html = requests.get(site).text
soup = BeautifulSoup(html, 'html5lib')

# find out more about what soup really is
# print(type(soup))
# print(soup.find_all('div', id=re.compile ('result'))) # bs4.element.resultset
# print(type(soup.select('div[id^=result]'))) # list

# let us try this once more
scrape = soup.find_all('div', id=re.compile('result'))
result = []
result2 = []
result3 = []
result4 = []
for div in scrape:
	#result.extend(div.find_all('img', alt=re.compile('')))
	result2.extend(div.find_all('a', {'class': "a-link-normal a-text-normal"}))
	result3.extend(link['href'] for link in div.findAll('a', href=re.compile('www.amazon.com/'))) # all the links
	result4.extend(div.find_all('span', {'class': 'a-offscreen'})) # find price
#print(result)
for line in result2:
	if line.find_all('span', {'class':'a-offscreen'}):
		print( line )
		for i in range(4):
			print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print(result3) links (a lot of redundant links)
# print(result4) prices (i am not sure if i grabbed them all)

# lets try to grab specifics
'''
print(soup.find('p', {'Data Science'})) # find all <p> {text} </p>
print(soup.div.p.text.split()) # turn p into a list
print(soup.p.get('id'))
print(soup('p'))
'''


# prompt everything worked
print("Successfully ran!")


# lets dig into another webpage huh?
#site = "https://www.amazon.com/What-Data-Science-Mike-Loukides-ebook/dp/B007R8BHAK"
#html = requests.get(site).text
#soup = BeautifulSoup(html, 'html5lib')
#scrape = soup.find_all('div')
#print(soup)

