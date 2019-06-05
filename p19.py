w= int(input())
l=[]
for i in range(q):
    l1=list(map(int,input().split()))
    for i in l1:
        l.append(i)
l.sort()
print(*l)