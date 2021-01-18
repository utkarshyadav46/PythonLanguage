#code challenge 20
x=[]   #declaring two list x and y
y=[]
j=0   
str1=raw_input("enter the string")  #taking string from user
x=list(str1)
l=len(str1)
l=l-1                           #taking length
while(l>=0):
    b=x[l]
    y.append(b)           #appending in a new list
    l=l-1
print ''.join(map(str,y))     #join by no space
