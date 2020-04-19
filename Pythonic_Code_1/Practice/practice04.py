# p 291, 04

user_dict = {}
user_list = ["students","superuser","professor","employee"]

for value1, value2 in enumerate(user_list):
    user_dict[value2] = value1

print(user_dict)
