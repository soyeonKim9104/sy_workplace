import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'} #필수로 불러오는 코드
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200407',headers=headers) #ajax의 url 불러오는 느낌

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 1

for music in musics:
    a_tag = music.select_one('td.info > a')
    if a_tag is not None:
        title = a_tag.text.strip()
        artist = music.select_one('td.info a.artist').text.strip()
        print(rank, title, artist)
        rank += 1
