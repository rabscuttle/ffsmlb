# Import
from splinter import Browser
from bs4 import BeautifulSoup as bs

# Splinter
executable_path = {'executable_path': 'c:/bin/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

# Get Prospects List
url = "https://www.prospects1500.com/top-50-lists-2020/"
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')

td = soup.findAll('td')
for t in td:
	url = t.findAll('a').text
	print(url)
