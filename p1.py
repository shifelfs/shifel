q=int(input())
li=[]
for i in range(0,q):
    i=input()
    li.append(i)
li1=[]
for i in zip(*li):
    if i.count(i[0])==len(i):
        li1.append(i[0])
    else:
        break
print(''.join(l1))