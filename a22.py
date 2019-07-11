l,m=map(int,input().split())
while m>l:
	l,m=m,l%m
print(l)