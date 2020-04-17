def test(t):
    print(x)
    t = 20 # local vaciable
    print("In function : ",t)

x = 10 # global variable
test(x)

print("In Main x is : ",x)
print("In Main t is : ",t) # can't use t out of the function 'test'.
