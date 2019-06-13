y=input()
b=''
for i in y:
    if i=="X":
        b+="A"
    elif i=="x":
        b+="a"
    elif i=="Y":
        b+="B"
    elif i=="y":
         b+="b"
    elif i=="Z":
        b+="C"
    elif i=="z":
        b+="c"
    else:
        b+=chr(ord(i)+3)
print(b)