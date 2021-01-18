#code challenge 06 
a=input("enter the numbers seperated with ,")
ls=list(a)
b=len(ls)
i=0
sum1=0
while i<b:
    if ls[i]!=13:
        sum1=sum1+ls[i]
        i=i+1
    elif ls[i]==13:
        i=i+2
        
print sum1
