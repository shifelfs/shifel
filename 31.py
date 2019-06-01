a=list(input())
a=a.replace(" ","")
count=0
for i in a:
	if(i!=' '):
		count=count+1
print(count)
