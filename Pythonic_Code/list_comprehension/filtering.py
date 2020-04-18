# filtering. if문과 함께 사용하는 list comprehension.

# 짝수만 저장하기

# 일반적인 반복문 + 리스트
result = []
for i in range(10):
    if i % 2 == 0 :
        result.append(i)
print("일반적인 반복문 + 리스트:",result)

# list comprehension
result = [i for i in range(10) if i % 2 == 0]
print("list comprehension:",result)

# if-else 뒤에 i의 값 할당 코드 위치
result2 = [i if i % 2 == 0 else 10 for i in range(10)]
print("list comprehension2:",result2)
