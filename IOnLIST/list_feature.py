# 하나의 리스트에 다양한 자료형 포함 가능
a = ["color",1,0.2]
print(a)
color = ['yellow','blue','green','black','purple']

# 중첩리스트
a[0] = color
print(a)

# way to store
l1 = [5,4,3,2,1]
l2 = [1,2,3,4,5]

l2 = l1
print(l2)

l1.sort() # 정렬
print(l2)

l2 = [6,7,8,9,10]
print(l1, l2)
