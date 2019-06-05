n,k=map(int,input().split())
l=list(map(int,input().split()))
ans=1
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		m=l[i]+l[j]
		if m==k:
			ans=0
if ans==0:
	print("yes")
else:
	print("no")
