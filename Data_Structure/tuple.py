# tuple 선언시 () 사용, list와는 다름
# list에서 사용하는 연산, 인덱싱, 슬라이싱 모두 동일하게 적용
t = (1,2,3)

print(t+t, t*2)

print(len(t))

# tuple의 값은 마음대로 변경 불가능 (error 발생)
t[1] = 5
