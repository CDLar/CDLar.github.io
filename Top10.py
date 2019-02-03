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

#Creating the Skater Dataframe with extended columns
fSkaters = pd.DataFrame(columns=['Name','Team','Position','FntPts'])
fSkaters['Name'] = dfF.Skaters.str[:-4]
fSkaters['Team'] = dfF.Skaters.str[-4:-1]
fSkaters['Position'] = dfF.Skaters.str[-1]
fSkaters['FntPts'] = dfF['Points']

#Checking for 2 letter team names
for x in fSkaters

#Changing the Fantasy Points column data type to float
fSkaters.replace('--','0',inplace=True)
fSkaters['FntPts'] = pd.to_numeric(fSkaters['FntPts'])


#Creating the Goalie Dataframe with extended columns
fGoalies = pd.DataFrame(columns=['Name','Team','Position','FntPts'])
fGoalies['Name'] = GdfF.Goalies.str[:-4]
fGoalies['Team'] = GdfF.Goalies.str[-4:-1]
fGoalies['Position'] = GdfF.Goalies.str[-1]
fGoalies['FntPts'] = GdfF['Points']

#Changing the Fantasy Points column data type to float
fGoalies.replace('--','0',inplace=True)
fGoalies['FntPts'] = pd.to_numeric(fGoalies['FntPts'])

#Merging the two extended Dataframes together then sort and reindex
fJoint = pd.concat([fSkaters,fGoalies])
fJoint.sort_values(by=['FntPts'],ascending=False,inplace=True)
fJoint.reset_index(drop=True, inplace=True)

print(fJoint)
print (fJoint[:10])