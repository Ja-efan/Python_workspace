# variable-length arguments
# 가변인수 : 매개변수의 개수가 정해지지 않고 진행해야 하는 경우 사용

def asterisk_test(a,b,*args): # *args가 가변인수
    return a + b + sum(args)

print(asterisk_test(1,2,3,4,5)) # 1,2는 각각 a,b에 3,4,5는 모두 *args에 할당

def asterisk_test2(a,b,*args):
    print (args)

asterisk_test2(1,2,3,4,5)
