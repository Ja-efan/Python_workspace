# set는 집합 연산 제공

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

#s1과 s2의 합집합
print(s1.union(s2))
print(s1 | s2)

#s1과 s2의 교집합
print(s1.intersection(s2))
print(s1 & s2)

#s1과 s2의 차집합(s1기준)
print(s1.difference(s2))
print(s1 - s2)
