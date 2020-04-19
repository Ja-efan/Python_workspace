# nested loop (중첩 반복문)
# list comprehension에서도 기존처럼 리스트 2개를 섞어 사용할 수 있다.

word_1 = "Hello"
word_2 = "World"

result = [i+j for i in word_1 for j in word_2] # 중첩 반복문
# word_1에서 나오는 값을 먼저 고정한 후, word_2의 값을 하나씩 가져와 결과 생성
print("nested loop:",result)


# nested loop + filtering
case_1 = ["A","B","C"]
case_2 = ["D","E","A"]
result = [i+j for i in case_1 for j in case_2 if i != j] # 반복문 끝에 if문 추가!!
print("nested loop + filtering:", result)
