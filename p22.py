n=int(input())
a=list(map(int,input().split()))
p=[]
q=[]
for i in range(len(a)):
	if i%2==0:
		p.append(a[i])
	else:
		q.append(a[i])
s=sum(p)
r=sum(q)
if(s>r):
	print(s)
else:
	print(r)
