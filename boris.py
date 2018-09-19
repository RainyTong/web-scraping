'''
This code is from borisChen's tutorial.
'''

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

base_url = 'http://www.qiushibaike.com/8hr/page/'

for num in range(1,5):

    print('第{}页'.format(num))

    r = requests.get(base_url + str(num), headers = headers)

    content = r.text
    soup = BeautifulSoup(content,'lxml')

  #  divs = soup.find_all(class_ = 'article block untagged mb15 typs_hot')
    divs = soup.find_all(class_ = 'content-block clearfix')

    print(divs)

    
    for div in divs:

        if div.find_all(class_ = 'thumb'):
            continue
        joke = div.span.get_text()
        author = div.h2.get_text()
        # votes = div.i.get_text()
    # stats = div.find_all(class_ = 'stats-vote')
    # stats_vote = stats.find_all(class_ = 'stats-vote')

        print(author)
        print(joke)
        # print(votes)
    # print(stats.get_text())
        print('----------')


