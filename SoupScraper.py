# import libraries
import requests
import bs4
from bs4 import BeautifulSoup
import csv

with open("blank.txt", "r") as blank:
    bReader =csv.reader(blank)
    bList =[]
    for row in bReader:
        if len (row) != 0:
            bList = bList + [row]

blank.close()

with open("Top10.txt", "w") as top10:
    tW = csv.writer(top10)
    for row in bList:
        tW.writerow([bList[row]])

top10.close()
