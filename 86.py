l=input().split()
for i in l:
	s=set(i)
	if len(s) == len(i):
		print("Yes")
	else:
		print("No")