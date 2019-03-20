import requests
from bs4 import BeautifulSoup as soup

class Headlines:
    """
    Object to contain the title, url, and text."""
    def __init__(self, otitle, olink):
        self.title = otitle
        self.link = olink
        self.article = []
    def get_Article(self):
        key = soup(requests.get(self.link).text, 'lxml')
        foo = key.find('div', {'class': 'storytext storylocation linkLocation'})
        xparagraph = foo.findAll('p')
        bar = []
        for x in xparagraph:
            bar.append(x.get_text())
        self.article = bar

sources = requests.get('https://www.npr.org/sections/news/').text

npr_soup = soup(sources, 'lxml')

data = npr_soup.find('div', {'class': 'list-overflow'})
titles = data.findAll('h2', {'class': 'title'})

xtitles = []
for t in titles:
    xtitles.append(t.get_text())

xlinks = []
for t in titles:
    foo = t.find('a')
    xlinks.append(foo.get('href'))

xheadlines = []
for t, l in zip(xtitles, xlinks):
    article = Headlines(t,l)
    xheadlines.append(article)

for x in xheadlines:
    x.get_Article()

def printInfo():
    for h in xheadlines:
        print(h.title)
        print(h.link)

#########################

print('----------')
printInfo()
print('----------')

file = open('articles.txt','w')

for x in xheadlines:
    file.write(str(x.title))
    file.write("\n")
    file.write(str(x.link))
    file.write('\n')
    for bar in x.article:
        file.write(str(bar))
