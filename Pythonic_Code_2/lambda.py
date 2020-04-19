# lambda func : 함수의 이름 없이, 함수처럼 사용할 수 있는 익명의 함수
# 3.x 버전부터는 람다 함수의 사용을 권장하지 않음

# 1
f = lambda x,y:x+y
print(f(1,4))

#2
print((lambda x,y:x+y)(1,4))
