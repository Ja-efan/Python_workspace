# enumerate() func
# 리스트의 값을 추출할 때 인덱스를 붙여 함께 출력하는 함수
print("<enumerate() func>")
for i, v in enumerate(['tic','tac','toc']): #리스트에 있는 인덱스와 값을 언패킹
    print(i,v)

# 주로 dictionary형으로, 인덱스를 키로, 단어를 값으로 하여
# 쌍으로 묶어 결과를 출력하는 방식을 사용
sentence = "TEAMLAB is an academic institue located in South Korea."
print({i:j for i,j in enumerate(sentence.split())})

#---------------------------------------------------------
print("-------------------------------------------------")
#---------------------------------------------------------

# zip() func
# 1개 이상의 리스트값이 같은 인덱스에 있을 때 병렬로 묶는 함수
print("<zip() func>")
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a,b in zip(alist, blist): #병렬로 값을 추출
    print(a,b)

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
sum = [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
print(sum)

for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)
    
