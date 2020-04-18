# set는 값을 순서 없이 저장하면서 중복을 불허하는 자료형
# tuple과 다르게 삭제나 변경 가능

s = set([1,2,3,1,2,3])
print(s)

s.add(8)
print(s)

s.remove(1)
print(s)

s.update([1,4,5,6,7])
print(s)

s.discard(3)
print(s)

s.clear()
print(s)
