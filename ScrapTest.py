from pandas.io.html import read_html
from selenium import webdriver
import time
import selenium


driver = webdriver.Chrome()
driver.get('http://fantasy.espn.com/hockey/league/scoreboard?leagueId=271')
time.sleep(5)
s1 = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[2]').text

print(score)

driver.close()