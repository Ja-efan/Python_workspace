# 기본적으로 dictionary는 순서를 보장하지 않는 객체
# OrderedDict는 순서를 가지는 dictionary 객체

from collections import OrderedDict

d = OrderedDict()

d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k,v in d.items():
    print(k,v)

print("-------------------------------------------------")
#---------------------------------------------------------

def sort_by_key(t):
    return t[0]

# value기준 정렬 함수
# def sort_by_value(t):
#     return t[1]

d2 = dict()
d2['x'] = 100
d2['y'] = 200
d2['z'] = 300
d2['l'] = 500

for k,v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
    print(k,v)

print(sorted(d.items(), key=sort_by_key))
