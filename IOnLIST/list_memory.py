kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score = [kor_score,math_score,eng_score]
print(midterm_score)

math_score[0] = 100

print(midterm_score)


# value vs offset
a = 300
b = 300

print(a is b) # 왜 true 나오지..?
print(a == b)

c = 1
d = 1

print(c is d)
print(c == d)
