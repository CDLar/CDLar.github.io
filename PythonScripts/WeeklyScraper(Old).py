from pandas.io.html import read_html
from selenium import webdriver
import time
import selenium
import csv
import pandas as pd

driver = webdriver.Chrome()
driver.get('http://fantasy.espn.com/hockey/league/scoreboard?leagueId=43185')
time.sleep(7)
s1 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(1) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--away:nth-child(1) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s2 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(1) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--home:nth-child(2) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s3 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(2) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--away:nth-child(1) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s4 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(2) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--home:nth-child(2) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s5 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(3) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--away:nth-child(1) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s6 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(3) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--home:nth-child(2) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s7 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(4) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--away:nth-child(1) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s8 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(4) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--home:nth-child(2) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s9 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(5) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--away:nth-child(1) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s10 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(5) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--home:nth-child(2) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s11 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(6) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--away:nth-child(1) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text
s12 = driver.find_element_by_css_selector('div.bp-mobileMDPlus.bp-mobileLGPlus.bp-tabletPlus.bp-desktopPlus.bp-desktopLGPlus div.jsx-813185768.shell-container:nth-child(5) div.page-container.cf:nth-child(2) div.layout.is-full:nth-child(1) div.layout__column.layout__column--1 div.jsx-1532665337.container.league-scoreboard-page.FHL--container.gameBorder div.jsx-3028651178.scoreboard.pt4 div.jsx-4239636790.matchup-score.h2h-points:nth-child(6) section.Scoreboard.bg-clr-white.flex.flex-auto.justify-between div.Scoreboard__RowContainer.flex.flex-column.flex-auto div.Scoreboard__Row.flex.w-100.Scoreboard__Row__Main div.jsx-4239636790.Scoreboard__Column.Scoreboard__Column--1.ph4.mv4:nth-child(1) div.jsx-4225632771.matchup-teams-score-container ul.ScoreboardScoreCell__Competitors.matchup-teams-score.status--in li.ScoreboardScoreCell__Item.flex.items-center.relative.pb2.ScoreboardScoreCell__Item--home:nth-child(2) > div.ScoreCell__Score.h4.clr-gray-01.fw-heavy.tar.ScoreCell_Score--scoreboard.pl2:nth-child(3)').text

S = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]
GM =['Larsen','Mann','Menna','Leis','Brawn','Snyder','Erlandson','Scheuermann','Sunny','KV','Buckley','Le Fevre']

#Play around with adding Win/loss and record later?
weeklyScores = pd.DataFrame({'GM':GM,'Score':S})

#print Weekly scores to CSV
weeklyScores.to_csv('WeeklyScores.csv')

driver.close()
print ('Finished')