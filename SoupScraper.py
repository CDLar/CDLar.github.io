# import libraries
import requests
import bs4
from bs4 import BeautifulSoup


req = requests.get('http://fantasy.espn.com/hockey/league/scoreboard?leagueId=43185')
soup = bs4.BeautifulSoup(req.text, 'lxml')

Score = soup.find_all('div',class_='ScoreCell__Score')
print(Score)
