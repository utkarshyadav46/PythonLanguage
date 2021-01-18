# code challenge 12
lis=[]
i=0
j=0
s=0
a=input("enter the number seperated by comma")#taking input from the user
lis=list(a)     
while i<=lis[0]: #till it matches first element
    j=0
    while j<=lis[1]:
        if(i*1+j*5)==lis[2]:  #condition for perfect match
            s=1
            print "True"
        j=j+1
    i=i+1
if(s==0):  #if condition dont match 
    print"False"

        
