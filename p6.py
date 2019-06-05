n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if z[i]<z[j]<z[k] and i<j<k:
                count=count+1
print(count)