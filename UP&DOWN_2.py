import random
from datetime import datetime

Choice = 0 # 메뉴 선택지 변수

# 기록파일 읽어오기
f = open("record_file.txt", 'r')
test = f.readlines()

if not test:    # 과거 기록이 없는 경우
    top = 11      # 최고기록 11로 지정, 첫번째 시도자의 점수는 무조건 최고점수
else:             # 과거 기록이 있는 경우
    score = int(test[0].split(' ')[0]) # 파일 내용 중 기록만 가져오기
    top = score                        # 과거 최고기록을 저장하여 최고기록 이어가기
f.close()

while True:
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    guess = random.randrange(1, 101)  # 범위=1~100 램덤 값(맞춰야되는 값)

    try:
        Choice = int(input(">>")) # 메뉴 선택지 입력
        if Choice < 1 or Choice > 3 :
            print("잘못 입력하셨습니다. 1,2,3 중에서 입력해주세요.")
            continue
    # 피드백 4) 메뉴에 해당하지 않는 번호(1,2,3이 아닌 번호)를 입력한 경우에는 다시 메뉴를 입력받기
    except:
        print("잘못 입력하셨습니다. 1,2,3 중에서 입력해주세요.")
        continue


    if Choice == 1: # 게임시작
        turn = 1 # 시도한 횟수 변수
        start = 1 # 범위 시작 = 1
        end = 100 # 범위 끝 = 100


        while turn < 11: # 시도 횟수 10번까지 가능
            number = int(input("%d번째 숫자 입력(%d~%d) :" % (turn, start, end)))  # 사용자가 입력한 수
            # 피드백 2) 정답으로 1~100 범위 안에 해당하지 않는 숫자는 입력 불가능하게 하기
            if number > 100 or number < 1:
                print("1~100사이의 수를 입력하세요.")
                continue

            if number > guess: # 사용자 입력값이 정답보다 크면 down 출력
                print("DOWN")
                # 피드백 1) 답 입력 후 범위가 축소된 경우 해당 범위에 속하지 않는 답을 입력하면 범위가 다시 늘어나지 않게 하기
                if number <= end:
                    turn += 1
                    end = number-1 # 범위 끝을 사용자 입력값-1으로 변경(입력값은 범위에서 제외하기 때문에-1)


            elif number < guess:  # 사용자 입력값이 정답보다 작으면 up 출력
                print("UP")
                # 피드백 1) 답 입력 후 범위가 축소된 경우 해당 범위에 속하지 않는 답을 입력하면 범위가 다시 늘어나지 않게 하기
                if number >= start:
                    turn += 1
                    start = number+1  # 범위 시작을 사용자 입력값+1으로 변경(입력값은 범위에서 제외하기 때문에 +1)

            elif number == guess: # 정답 맞춤
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %turn)
                # 피드백 3) 최고기록인 경우에만 기록에 추가해주기
                if turn < top: # 시도횟수가 최고기록보다 크면 최고기록 갱신
                    print("최고기록 갱신~!")
                    top = turn
                    nickname = input("닉네임을 입력헤주세요:")
                    record = "%d %s %s\n" % (turn, nickname, datetime.today().strftime("%Y.%m.%d")) # 파일에 인덱스, 닉네임, 날짜 기록
                    f = open("C:/Users/yp122/PycharmProjects/SWING2-2/record_file.txt", 'a')
                    f.write(record) # txt파일에 저장
                    f.close()
                    break
                else:
                    break



    elif Choice == 2: # 기록확인
        f = open("C:/Users/yp122/PycharmProjects/SWING2-2/record_file.txt", 'r')
        r = f.readlines() # 파일에서 기록 읽어오기
        ranking = 1 # 순위 변수
        for s in r: # 기록 출력
            print("%d %s" % (ranking, s))
            ranking += 1
        f.close()


    elif Choice == 3:   # 게임종료
        break
