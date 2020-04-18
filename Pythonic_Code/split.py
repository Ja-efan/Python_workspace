# split() 문자열의 값을 특정 값을 기준으로 분리하여 리스트 형태로 변환하는 함수

items = 'zero one two three'.split()
print(items)

# ","을 기준으로 문자열 나누기
example = 'python,jquery,javascript'
print(example.split(","))

#리스트에 있는 각 값을 a,b,c에 언패킹
a,b,c = example.split(",")
print(a,b,c)

example = "theteamlab.univ.edu"
# "."을 기준으로 문자열 나누기 -> 언패킹
subdomain,domain,tld = example.split(".")
print(subdomain,domain,tld)
