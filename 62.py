a=input()
n=len(a)
count=0
for i in a:
	if (i=='1' or i=='0'):
		count=count+1
if(count==n):
	print("yes")
else:
	print("no")