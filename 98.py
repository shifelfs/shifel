n=int(input())
k=list(map(int,input().split()))
for i in range (0,n-1):
	if(k[i]!=i+1):
		print(i)
		break