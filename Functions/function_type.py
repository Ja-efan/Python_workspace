# parameter x, return x
def a_rectangle_area():
    print (5*7)

# parameter o, return x
def b_rectangle_area(x,y):
    print (x*y)

# parameter x, return o
def c_rectangle_area():
    return (5*7)

# parameter o, return o
def d_rectangle_area(x,y):
    return (x*y)

a_rectangle_area()
b_rectangle_area(5,7)
print(c_rectangle_area())
print(d_rectangle_area(5,7))
