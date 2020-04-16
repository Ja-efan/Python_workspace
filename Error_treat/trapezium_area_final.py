def addition(x,y):
    return x+y

def divided_by_2(x):
    return x / 2

def main() :
    base_line = float(input("밑변의 길이 : "))
    upper_line = float(input("윗변의 길이 : "))
    height = float(input("높이 : "))

    print ("사다리꼴의 넓이는 ", divided_by_2(addition(base_line,upper_line))*height)


if __name__ == '__main__':
    main()
