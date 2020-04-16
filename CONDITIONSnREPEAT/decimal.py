# 십진수의 이진수 변환

print("이진수로 변환할 십진수 입력. ")

decimal = int(input())
result = ""

while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result

print(result)
