def asterisk_test(*args):
    x,y,*z = args
    return x,y,z

print(asterisk_test(3,4,5))

## result :  (3,4,[5]) 
