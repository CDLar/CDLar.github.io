# import libraries
import requests
import bs4
from bs4 import BeautifulSoup


req = requests.get('http://www.espn.com/nhl/scoreboard?date=20181102')
soup = bs4.BeautifulSoup(req.text, 'lxml')
scores = []
names = []
for i in soup.select('.team-score'):
    scores.append(i.text)

for i in soup.select('.team-name'):
    names.append(i.text)    

newNames = [names[0],names[2],names[6],names[8],names[12],names[14]]

final = zip(newNames,scores)

print(list(final))