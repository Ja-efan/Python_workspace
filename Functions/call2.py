def spam(eggs):
    eggs.append(1)
    eggs = [2,3] # eggs에 새로운 값 할당 (주소값 변경)
    #return (eggs)
ham = [0]

spam(ham)
print(ham)

#print(spam(ham))
