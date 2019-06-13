n=int(input())
count=0
a=[]
for i in range(n):
    a.append(input())
for i in range(n):
    if sorted(a[i])==sorted('kabali'):
        count=count+1
print(count)        
