from selenium import webdriver
from pandas.io.html import read_html
import chromedriver
import pygsheets
import time


driver = webdriver.Chrome()
driver.get(f'http://fantasy.espn.com/hockey/team?leagueId=271&seasonId=2019&teamId=1&statSplit=last15')
time.sleep(5)
# Skaters
table = driver.find_element_by_xpath('//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[3]')
table_html = table.get_attribute('innerHTML')
df = read_html(table_html)[0]  # read table
print(df)    # write to sheet

driver.close()