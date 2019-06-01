a,b=input().split()
a=int(a)
b=int(b)
for num in range(a+1,b):
	for j in range(2,num):
           
		if (num % j) == 0:
              
			break
       
	else:
          
 		print(num,end=" ")