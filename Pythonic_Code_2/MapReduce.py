# MapReduce : 빅데이터를 처리하기 위한 기본 알고리즘

# map() func
# 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용

ex = [1,2,3,4,5]
f = lambda x:x**2
f2 = lambda x,y:x+y
print(list(map(f,ex))) # (f,ex) 불가

for value in map(f,ex):
    print(value)

print(list(map(f2,ex,ex)))


# filtering
print(list (map(lambda x:x**2 if x%2==0 else x, ex))) # by map()
print([x**2 if x%2==0 else x for x in ex]) # by list comprehension

# reduce() func 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수

from functools import reduce

print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
