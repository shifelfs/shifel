a=input()
mid=len(a)//2
if len(a)%2!=0:
    for i in range(len(a)):
        if i==mid:
            print("*",end="")
        else:
            print(a[i],end="")
else:
    for i in range(len(a)):
        if i==mid or i==mid-1:
            print("*",end="")
        else:
            print(a[i],end="")
                    
