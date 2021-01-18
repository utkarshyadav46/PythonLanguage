#Chakravarthi_Parripati
#week2_Submission 7
#dealing with dictionary type of variable
st=raw_input()
#This takes input from user
lt=set(st)
d={}
#this is the decleration of empty dictionary variable
for i in lt:
    d[i]=st.count (i)    
print d
