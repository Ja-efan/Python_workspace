alist = ['a','b','c']
blist = ['1','2','3']
abcd = []

abc = []
#abc= [[a,b] for a,b in enumerate(zip(alist,blist))]
abc.append('a'[0])
print(abc)

for a,b in enumerate(zip(alist,blist)):
    try :
        abcd.append(b[a])
        print(b)
    except IndexError:
        abcd.append("error")

print(abcd)
