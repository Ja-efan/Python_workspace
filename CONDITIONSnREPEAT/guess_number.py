import random

random_num = random.randint(1,100)

print("숫자를 맞춰 보세요.(1~100)")

input_num = int(input())

while(input_num != random_num):
    if random_num > input_num:
        print("UP!!")
    else:
        print("Down!!")
    input_num = int(input())

else :
    print("Correct!! 정답은 ",input_num," 입니다.")
