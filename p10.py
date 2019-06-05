p=int(input())
c7=0
r=list(map(int,input().split()))
for y in range(0,p):
  for x in range(0,y):
    if(r[x]<r[y]):
      c7=c7+r[x]
print(c7)