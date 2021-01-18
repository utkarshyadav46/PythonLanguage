#code challenge 18
#this code works on the principle of recursion
#this is the program of printing the pascal triangle 
def pascal(n):   #defining a function
    if n==0:      
        return []
    elif n==1:      
        return [1]
    else:
        new=[1]
        last=pascal(n-1)    #find the last row
        for i in range(len(last)-1):
            new.append(last[i] + last[i+1])#append till the range defined
        new = new+[1]
    return new

n=input("enter the number of row ")   #taking number of rows from user
c=[]              #declaring a list
i=1

while i<=n:
    c=pascal(i)   #calling the pascal function
    print c       #printing the element of c
    i=i+1
