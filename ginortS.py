#string arranging
st = input()
st = sorted(st,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x))
print(*(st),sep = '')
