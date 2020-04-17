# 키워드 인수 : 함수에 입력되는 매개변수의 변수명을 사용하여 함수의 인수를 지정

def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name,my_name))

print_something("Jaehwan","TeamLab")
print_something(your_name="TeamLab",my_name="Jaehwan")
