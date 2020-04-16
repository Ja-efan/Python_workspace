# indexing
colors = ["red","blue","green"]
print(colors[0])
print(colors[1])
print(colors[2])
print(len(colors))

# slicing
cities = ['서울','부산','인천','대구','대전','광주','울산','청주']
print(citis[0:6])

# reverse index
print(cities[-8:])

# slicing with over index
print(cities[:])
print(cities[-50:50])

# step(증가값)
print(cities[::2])
print(cities[::-1]) // 역방향으로 증가값 실행

# add operate
color1 = ['red','blue','green']
color2 = ['orange', 'black', 'white']
print(color1+color2)
print(len(color1))
total_color = color1 + color2
print(total_color)
print(len(total_color))

# multiply operate
color1_2 = color1 * 2
print(color1_2)

# in operate
print('blue' in color2)
