a=input("enter the numbers seperated with ,")
ls=list(a)
ls.sort()
ls.pop()
ls.pop(0)
b=0
i=0
c=len(ls)
while i<c:
    b=b+ls[i]
    i=i+1
b=b/i
print b

    
