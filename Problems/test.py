import requests
website_url = requests.get('https://en.wikipedia.org/wiki/Demographics_of_Italy').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

My_table = soup.find_all('table', attrs={"class": "wikitable sortable"})