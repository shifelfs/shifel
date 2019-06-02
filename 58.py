n,k=map(int,input().split())
a=map(int,input().split())
count=0
for i in a:
	if(i==k):
		count=count+1
if(count>0):
	print("yes")
else:
	print("no")