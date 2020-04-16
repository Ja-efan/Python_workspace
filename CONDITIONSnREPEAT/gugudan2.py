print("출력할 단 선택(1~9), 0 종료")

dan = 1
while(dan != 0):

    dan = int(input())

    if dan == 0: break

    elif dan>9 or dan<1 :
        print("1~9 중에 입력해 주세요.")
        continue

    else:
        for i in range (1,10):
            print(dan, 'x' , i , '=', dan*i)
        print("다음으로 출력할 단을 입력하세요.(1~9)")

print("구구단을 종료합니다.")
