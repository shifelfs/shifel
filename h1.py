n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
s=set(l)
if len(l)==len(s):
	print("unique")
else:
	for i in range(len(l)):
		if l[i] not in a:
			a.append(l[i])
		else:
			b.append(l[i])
c=set(b)
print (*c)
