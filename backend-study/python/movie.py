import requests
from bs4 import BeautifulSoup

# pymongo 기본 셋팅
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 타겟 url을 읽어서 html를 받아오기
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'} #필수로 불러오는 코드
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers) #ajax의 url 불러오는 느낌

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 "이 담긴 상태가 됨

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
rank = 1
for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None: # 참일 경우
        title = a_tag.text
        star = movie.select_one('td.point').text
        print(rank,title,star)

        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }

        db.movies.insert_one(doc)
        rank += 1