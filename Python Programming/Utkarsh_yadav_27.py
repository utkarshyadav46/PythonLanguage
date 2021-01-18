#2016kucp1023
#code challenge 4
#subimission 27
k=[]                #declaring a list
while(1):                     
    count1,count2,count3=0,0,0   #declaring  counters
    a=raw_input("")         #taking input from users
    if(a==""):              #continue til user give blank input
        break
    
    b=a.split("@")          #checking @condition
    for i in b[0]:             
        if(i.isalpha()!=True and i.isdigit()!=True and i!="_" and i!="-"):
            count1=1          
            

    c=b[1].split(".")      #check the condition 2 of (.)
    for i in c[0]:
        if(i.isalpha()!=True and i.isdigit()!=True):
            count2=1
            

    if(len(c[1])>3):    # checking the extension 
        count3=1
         
    if(count1!=1 and count2!=1 and count3!=1):
        k.append(a)    #appending all the valid email in list 
print k      #printing the list
         
         
        
    
