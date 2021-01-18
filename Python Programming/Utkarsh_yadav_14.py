#code challenge 14
# this code majorly based on dictionary data structre
def teen_condition(x):# function for checking the condition for range (13,19)
    if x==15 or x==16:
        return x
    elif x in range(13,19):
        return 0 #as given in the program
def add(valu):
    s=0
    for i in valu:# if the value is not in the range13 to 19
        if i not in range(13,20):
            s=s+i# simply add
        else:
            f_value=teen_condition(i)  #if not then check the condition by calling teen condition function
            s=s+f_value
    print "sum is",s     # final sum
        
valu=[]
a=input("enter the input")
valu=list(a.values())    
add(valu)                        # calling add function

