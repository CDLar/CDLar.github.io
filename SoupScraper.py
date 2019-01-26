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
time.sleep(2)

driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/label[4]').click()
time.sleep(2)

GnameTable = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/section[1]/table[1]/tbody[1]/tr[1]/td[1]')
GscoreTable = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]/section[1]/table[1]/tbody[1]/tr[1]/td[3]')
Gname_html = GnameTable.get_attribute('innerHTML')
Gscore_html = GscoreTable.get_attribute('innerHTML')

dfScore = read_html(score_html)[0]
dfName = read_html(name_html)[0]
dfS = pd.DataFrame(dfScore, columns = ['Points'])
dfN = pd.DataFrame(dfName, columns = ['Skaters'])
dfF = dfF = pd.concat([dfN,dfS], axis=1, ignore_index = True)
dfF.columns = ['Skaters', 'Points']

GdfScore = read_html(Gscore_html)[0]
GdfName = read_html(Gname_html)[0]
GdfS = pd.DataFrame(GdfScore, columns = ['Points'])
GdfN = pd.DataFrame(GdfName, columns = ['Goalies'])
GdfF = GdfF = pd.concat([GdfN,GdfS], axis=1, ignore_index = True)
GdfF.columns = ['Goalies', 'Points']


driver.close()
t10 = dfF.append(GdfF, ignore_index=false)
 
print(dfF[:10])
print(GdfF[:10])
print(t10)

#with open("Top10.txt", "w") as top10:
    #tW = csv.writer(top10)
    #for i in range(10):
       # tW.writerow([dfF(i)])

#top10.close()

