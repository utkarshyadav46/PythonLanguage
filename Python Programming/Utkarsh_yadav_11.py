# code challenge 11
#to complete this assignment we can use reduce function to add
def Sum(x,y):return x+y                          #define add function
def Multiply(x,y): return x*y                     #define multiply
def Largest(x,y):                                 #define largest function
    if x>y:
        return x
    else:
        return y
def Smallest(x,y):                               # define smallest function to find smallest number
    if x>y:
        return y
    else:
        return x
def Remove_Duplicates(lis):                              #remove funcion to remove duplicate number in a list
    y={}
    z=[]
    y=set(lis)
    z=list(y)
    return z
def Sort(lis):                              #sorting function to sort element using bubble sorting
    for i in range(len(lis)):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]        #swaping of two numbers 
    return lis  
         
def Print(lis):                                           #print function declared
    print"Sum = ",reduce(Sum,lis)
    print "Multiply = " ,reduce(Multiply,lis)
    print "Largest = " ,reduce(Largest,lis)
    print "Smallest = ", reduce(Smallest,lis)
    print "Sorting = ", Sort(lis)
    print "Without_duplicate = ",Remove_Duplicates(lis)
    
    
lis=[]                                #declaration of list
x=input("enter the numbers seperated by comma");
lis=list(x)
                                   
Print(lis)


