import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mymoviestar

def get_urls():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')

    urls=[]
    for tr in trs:
        a = tr.select_one('td.title > a')
        if a is not None:
            baseurl = 'https://movie.naver.com/'
            url = baseurl + a['href']
            urls.append(url)

    return urls

def insert_star(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
    recent = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text

    doc = {
        'name' : name,
        'img_url' : img_url,
        'recent' : recent,
        'url' : url,
        'like' : 0
    }

    db.mystar.insert_one(doc)
    print('완료', name)

def insert_all():
    db.mystar.drop()  # mystar 콜렉션을 모두 지워줍니다
    urls = get_urls()
    for url in urls:
        insert_star(url)


insert_all()
