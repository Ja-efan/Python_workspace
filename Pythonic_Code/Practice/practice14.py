alphabet = ['a','b','c','d','e','f','g','h']
nums = [i for i in range(20)]

answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2 ==0]
print(len(answer))
print(answer)
