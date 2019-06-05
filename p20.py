n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
c9=0
for i in range(0,len(l)):
	if k>=l[i]:
	    s=k//l[i]
	    c9=c9+s
	k=k%l[i]
	if k==0:
		break
print(c9)