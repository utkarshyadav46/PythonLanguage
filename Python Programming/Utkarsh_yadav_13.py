#code challenge 13
# this is to print the star pattern
n=input("enter the number of line ")#take the iteger input
for i in range(1,n+1):    #this loop is for priting half above pattern
    print i * "* "
for j in range(n-1,0,-1):     #this loop is for printiing below half pattern 
    print j * "* "
#this loop is for printing another half pattern
