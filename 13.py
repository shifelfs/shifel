num = int(input())
if num > 1:  
   for i in range(2, num//2): 
       if (num % i) == 0: 
           print("yes") 
           break
else: 
   print("no") 
