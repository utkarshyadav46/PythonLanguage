#code challenge 18
c=0
alpha="abcdefghijklmnopqrstuvwxyz"  #taking the alphabet
str1=raw_input("enter the string")   #taking strig from user
s=str1.lower()            #convert it into lower case
str2=set(s)
str3=list(str2)          #convert it into list
for j in str3:
    if j in alpha: 
        c=c+1
           
if (c==26):
    print "PANGRAM"
else:
    print "NOT PANGRAM"

