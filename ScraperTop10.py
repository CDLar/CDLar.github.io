from pandas.io.html import read_html
from selenium import webdriver 
import time
import selenium
import pandas as pd
import csv

driver = webdriver.Chrome()
driver.get(f'http://fantasy.espn.com/hockey/players/add?leagueId=43185&seasonId=2019&view=stats&statSplit=last7')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="filterStatus"]/option[5]').click()
time.sleep(5)
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/section[1]/table[1]/tbody[1]/tr[1]/td[3]/table[1]/thead[2]/tr[1]/th[1]/div[1]/span[1]').click()
time.sleep(2)
nameTable = driver.find_element_by_xpath('//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div[2]/section/table/tbody/tr/td[1]')
scoreTable = driver.find_element_by_xpath('//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div[2]/section/table/tbody/tr/td[3]')
name_html = nameTable.get_attribute('innerHTML')
score_html = scoreTable.get_attribute('innerHTML')


dfScore = read_html(score_html)[0]
dfName = read_html(name_html)[0]
dfS = pd.DataFrame(dfScore, columns = ['Points'])
dfN = pd.DataFrame(dfName, columns = ['Skaters'])
dfF = dfF = pd.concat([dfN,dfS], axis=1, ignore_index = True)
dfF.columns = ['Skaters', 'Points']
driver.close()

print(dfF)


#with open("Top10.txt", "w") as top10:
    #tW = csv.writer(top10)
    #for i in range(10):
       # tW.writerow([dfF(i)])

#top10.close()

