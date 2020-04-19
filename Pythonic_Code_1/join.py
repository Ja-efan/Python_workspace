# join() 문자열로 구성된 리스트를 합쳐 하나의 문자열로 반환하는 함수

colors = ['red','blue','green','yellow']
result = ''.join(colors)
print(result)

result2 = ' '.join(colors) # 연결 시, 1칸을 띄고 연결
print(result2)

result3 = ','.join(colors) # 연결 시, ","으로 연결
print(result3)

result4 = '-'.join(colors) # 연결 시, "-"으로 연결
print(result4)
