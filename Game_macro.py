from selenium import webdriver

path = "C:\chromedriver.exe"       # 웹드라이버 경로
driver = webdriver.Chrome(path)    # 웹드라이버 경로 지정하기

driver.get("http://zzzscore.com/1to50/") # 브라우저 열기
buttons = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]') # 버튼가져오기
num = 1

for i in range(1, 51):   # 50개의 버튼 누르기
    for k in buttons:
        if k.text == str(num):  # 버튼번호와 횟수변수값이 같을 경우 클릭한다
            k.click()
            num += 1
            print("Click" + str(num))
