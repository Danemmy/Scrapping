from bs4 import BeautifulSoup
import requests

source = requests.get('https://pl.indeed.com/jobs?q=entry+level&l=Polska').text

soup = BeautifulSoup(source, 'lxml')

for h2 in soup.find_all('h2', class_='title'):
    #print(h2.prettify())

    title = h2.a.text

    print (title)