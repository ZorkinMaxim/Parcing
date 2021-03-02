import requests
from bs4 import BeautifulSoup
from time import sleep

url = 'http://telemetr.me/channels'

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }
    resp = se.get(url)

index = BeautifulSoup(resp.content, 'html.parser')

max_page = int(input('Input approximative page number: '))
pages = []
input_category = input('Input category: ')

for x in range(1, max_page + 1):
    sort = pages.append(se.get(f'http://telemetr.me/channels/cat/{input_category}/?page=' + str(x)))

for sort in pages:
    pars = BeautifulSoup(sort.content, 'html.parser')

    for el in pars.select('.wd-300'):
        link = el.find('a')
        print(link.get('href'))
