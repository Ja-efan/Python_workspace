def f():
    global s
    s = "I love Paris!"
    print(s)

s = "I love London!"
f()
print(s)
