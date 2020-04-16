print("태어난 연도 입력 : ")

year = int(input())

age = 2020 - year + 1

if 20<=age<=26 : # age <= 26 and age >=20
    student = '대학생'
elif 17<=age<20 : # age < 20 and age >=17
    student = '고등학생'
elif 14<=age<17 : # age < 17 and age >= 14
    student = '중학생'
elif 8<=age<14 : # age < 14 and age >= 8
    student = '초등학생'
else : student = '학생이 아닙니다.'

print(student)
