import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

base_url = 'https://gleague.nba.com/news/#news-archive-list_navigation'

r = requests.get(base_url, headers=headers)

content = r.text

soup = BeautifulSoup(content,'lxml')

divs = soup.find_all(class_='secondary-header news-archive-header')

#divs = soup.find_all(class_='news-archive-list')

print(divs)


'''for div in divs:

    headlines = div.h2.get_text()
    print(headlines)
    print('-------------')'''
