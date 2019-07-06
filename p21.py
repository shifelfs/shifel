a=int(input())
l=list(map(int,input().split()))
avg=int(a/2)
list1=l[:avg]
list2=l[avg::]
if ((sum(list1)//len(list1))==(sum(list2)//len(list2))):
    print("yes")
else:
    print("no")