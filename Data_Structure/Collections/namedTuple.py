# namedtuple은 튜플의 형태로 데이터 구조체를 저장하는 방법.
# 어떤 특정 데이터는 저마다 규정된 정보가 있다.
# c의 struct와 동일..?

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(11,y=22)
print(p)

print(p.x,p.y)
