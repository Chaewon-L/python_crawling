import urllib.request
from bs4 import BeautifulSoup

web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n")
print("학과                 홈페이지")

d_name = soup.findAll("a")      # a태그 내용 추출

for k in d_name:
    # 출력범위 제한하기(대학원, 교양대학, 자율전공학부는 제외)
    if k.text == "자율전공학부" or k.text == "교양대학" or "대학원" in k.text:
        continue

    else:
        link = urllib.request.urlopen("http://www.swu.ac.kr" + k['href'])
        d_soup = BeautifulSoup(link, 'html.parser')
        d_url = d_soup.find('a', {"class", "btn btn_xl btn_blue_gray"})


        if d_url:      #링크있는 경우 = 학과+홈페이지 주소 출력
            if "홈페이지" in d_url.text:
                print(k.text + "\t\t\t" + d_url['href'])
            else:      #홈페이지링크 없는 경우 = 학과+홈페이지 존재하지 않음 출력
                print(k.text + "\t\t\t" + "홈페이지가 존재하지 않음")


        else:          #링크 없는 경우 = 학과+홈페이지 존재하지 않음 출력
            print(k.text + "\t\t\t" + "홈페이지가 존재하지 않음")
