a=input().split()
for i in a:
	s=set(i)
	if len(s) == len(i):
		print("Yes")
	else:
		print("No")
