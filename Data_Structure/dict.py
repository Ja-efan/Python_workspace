country_code = {"America":1, "Korea":82, "China":86, "Japan":81}
print(country_code)

# dictionary의 key 반환
print(country_code.keys())

# dictionary의 value 반환
print(country_code.values())

# dictionary의 key-value pair 반환
print(country_code.items())

print('----------------------------------')
# 실제 dictionary를 사용할 때는 for문과 함께 사용
for k,v in country_code.items():
    print("Key: ",k)
    print("Value: ",v)
