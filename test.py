
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://gleague.nba.com/news/')

html = driver.page_source
soup = BeautifulSoup(html,features="lxml")

# check out the docs for the kinds of things you can do with 'find_all'
# this (untested) snippet should find tags with a specific class ID
# see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
tags = soup.find_all("h2", class_="archive-item-info__title")
# print(tags)
for tag in tags :
    print(tag.text)