
import json as js
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

url = 'https://www.nba.com/timberwolves/news/load_more/page/'

for i in range(1,100):

    base_url = url + str(i)

    r = requests.get(base_url)

    content = r.content.decode()

    dict_json = js.loads(content)

# print(dict_json['content'])
    html = dict_json['content']

    soup = BeautifulSoup(html,'lxml')

    divs = soup.find_all(class_ = 'post__title')

# print(divs)


    for div in divs:
        headlines = div.a.get_text()
        print(headlines)



# soup = BeautifulSoup(content,'lxml')
#
# divs = soup.find_all(class_ = 'post__title')
# # print(divs)
# for div in divs:
#     headlines = div.a.get_text()
#     print(headlines)
#     print('-------------')
