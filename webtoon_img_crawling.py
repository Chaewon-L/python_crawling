import urllib.request
from bs4 import BeautifulSoup
import os

# 오프너 객체생성하여 헤더추가
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

#가져올 웹툰 주소
web = urllib.request.urlopen("https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu")
soup = BeautifulSoup(web, 'html.parser')


#디렉토리 생성(있으면 기존디렉토리 사용, 없으면 새로 생성)
if not os.path.isfile("독립일기"):
    os.mkdir("독립일기")
    os.chdir("독립일기")
else:
    os.chdir("독립일기")

#회차 확인
episode = soup.findAll("td",{"class":"title"})

for i in episode:
    page = urllib.request.urlopen("https://comic.naver.com" + i.a['href'])
    soup2 = BeautifulSoup(page, "html.parser")

    episode2 = soup2.find("div", {"class", "wt_viewer"})
    e_img = episode2.findAll("img")
    count = 1

    e_name = i.find('a').text # 각 회차 제목가져오기
    os.mkdir(e_name) # 회차 제목 디렉토리 생성
    os.chdir(e_name) # 해당 디렉토리로 이동

    for k in e_img:
        urllib.request.urlretrieve(k['src'], str(count)+".jpg") #url 주소의 문서 다운로드
        count += 1

    os.chdir('..') #이전 디렉토리로 이동

print("이미지 저장 완료")
