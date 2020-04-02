import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('.list-wrap > tbody > tr')

rank = 1
for music in musics:
    m_title = music.select_one('td.info > a')
    # print(m_title)
    if m_title is not None:  # None은 참
        title = m_title.text.lstrip() #white space제거 함수 ex)오른쪽 : rstrip
        artist = music.select_one('td.info .artist').text.lstrip()
        print(rank,title,artist)
        rank += 1

