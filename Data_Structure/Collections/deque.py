# deque 모듈은 스택과 큐를 모두 지원하는 모듈.

from collections import deque

# deque_list를 deque로 선언...?
deque_list = deque()

for i in range(5):
    deque_list.append(i)

print("deque_list:",deque_list)

print("deque_list pop():" , deque_list.pop()) # 마지막에 들어간 값 반환

print("deque_list:",deque_list)

#---------------------------------------------------------
print("-------------------------------------------------")

# deque에서 queue사용 방법.
# 새로운 값을 왼쪽부터 입력하여 먼저 들어간 값부터 출력 될 수 있도록 한다.

deque_list2 = deque()

for i in range(5):
    deque_list2.appendleft(i)

print("deque_list2: ",deque_list2)

#---------------------------------------------------------
print("-------------------------------------------------")

# deque의 rotate()
deque_list3 = deque()

for i in range(5):
    deque_list3.append(i)

print("deque_list3:",deque_list3)

deque_list3.rotate(2)
print("deque_list3.rotate(2):", deque_list3)

deque_list3.rotate(2)
print("deque_list3.rotate(2):", deque_list3)

#---------------------------------------------------------
print("-------------------------------------------------")

# deque's feature
# reserved(), extend(), extendleft()..

print("deque_list3:",deque_list3)
print("reversed deque_list3:",deque(reversed(deque_list3)))

print("deque_list3:",deque_list3)
deque_list3.extend([5,6,7])
print("extend deque_list3:", deque_list3)

print("deque_list3:", deque_list3)
deque_list3.extendleft([5,6,7])
print("extendleft deque_list3:", deque_list3)
