words = "The quick brown fox jumps over the lazy dog".split()
print(words)

# 리스트의 각 요소를 대문자, 소문자, 길이로 변환하여 이차원 리스트로 변환
# 대괄호 2개 사용
stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print(i)

#---------------------------------------------------------
print("-------------------------------------------------")
#---------------------------------------------------------

# for문 2개를 사용한 two dimensional list
# 대괄호 2개 사용. 먼저 작동 하는 for문의 순서가 달라진다.
# case_2의 첫번째 요소인 D가 고정되고 case_1의 요소가 하나씩 앞에 붙는다.

case_1 = ["A","B","C"]
case_2 = ["D","E","A"]
result = [[i+j for i in case_1] for j in case_2]
# result = [i+j for i in word_1 for j in word_2]와 구분 해야한다.
print(result)
