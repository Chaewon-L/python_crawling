import random

choice = 0 # 메뉴 선택지 변수
score = [] # 기록 리스트
top = 11 # 최고기록 11로 지정, 첫번째 시도자의 점수는 무조건 최고점수

while True:
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    Choice = int(input(">>")) # 메뉴 선택지 입력
    guess = random.randrange(1, 101)  # 범위=1~100 램덤 값(맞춰야되는 값)

    if Choice == 1: # 게임시작
        turn = 1 # 시도한 횟수 변수
        start = 1 # 범위 시작 = 1
        end = 100 # 범위 끝 = 100


        while(turn < 11): #시도 횟수 10번까지 가능
            number = int(input("%d번째 숫자 입력(%d~%d) :" % (turn, start, end)))  # 사용자가 입력한 수

            if number > guess: # 사용자 입력값이 정답보다 크면 down 출력
                print("DOWN")
                turn += 1
                end = number-1 # 범위 끝을 사용자 입력값-1으로 변경(입력값은 범위에서 제외하기 때문에-1)

            elif number < guess: # 사용자 입력값이 정답보다 작으면 up 출력
                print("UP")
                turn += 1
                start = number+1  # 범위 시작을 사용자 입력값+1으로 변경(입력값은 범위에서 제외하기 때문에 +1)

            elif number == guess: # 정답 맞춤
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %turn)
                score.append(turn) # 기록을 기록 리스트에 추가
                if turn < top: # 시도횟수가 최고기록보다 크면 최고기록 갱신
                    print("최고기록 갱신~!")
                    top = turn #
                break


    elif Choice == 2: # 기록확인
        score.sort() # 기록 리스트 정렬
        ranking = 1
        for s in score: # 기록 출력 (순위 점수)
            print("%d %d" % (ranking, s))
            ranking += 1


    else:   # 그 외의 메뉴선택지이면 게임종료
        break
