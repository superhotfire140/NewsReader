import requests
from bs4 import BeautifulSoup as soup

source = requests.get('https://www.npr.org/sections/news/').text

npr_soup = soup(source, 'lxml')

data = npr_soup.find('div', {'class': 'list-overflow'})
titles = data.findAll('h2', {'class': 'title'})

def printInfo():
    for t in titles:
        print(t.get_text())


print('----------')
printInfo()
print('----------')


file = open('articles.txt','w')
for t in titles:
    file.write(str(t.get_text()))
    file.write('\n')
    file.write(str('----------'))
    file.write('\n')
