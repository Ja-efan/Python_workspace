# list comprehension : 기존 리스트형을 사용하여 간단하게 새로운 리스트를 만드는 기법

# 일반적인 반복문 + 리스트
result = []
for i in range(10):
    result.append(i)
print("일반적인 반복문 + 리스트:",result)

# list comprehension
result = [i for i in range(10)]
print("list comprehension:",result)
