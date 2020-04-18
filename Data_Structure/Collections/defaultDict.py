# defaultDict모듈은 딕셔너리의 변수를 생성할 때 키에 기본 값을 지정하는 방법
# 새로운 키를 생성할 때 별다른 조치 없이 신규 값을 생성할 수 있다.

from collections import defaultdict


# default == int

int_dict = defaultdict(int)
print(int_dict)
print(int_dict['key1'])

int_dict['key2'] = 'test'
print(int_dict)

#---------------------------------------------------------
print("-------------------------------------------------")
#---------------------------------------------------------

# default == list

list_dict = defaultdict(list)
print(list_dict)
print(list_dict['key1'])

list_dict['key2'] = 'test' # 값을 지정하면 해당 값으로 초기화
print(list_dict)

#---------------------------------------------------------
print("-------------------------------------------------")
#---------------------------------------------------------

# default == set

set_dict = defaultdict(set)
print(set_dict)
print(set_dict['key1'])

set_dict['key2'] = 'test'
print(set_dict)
