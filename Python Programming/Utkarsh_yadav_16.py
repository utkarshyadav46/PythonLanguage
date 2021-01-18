#code challenge 16
def translate(str1):
    x=[]    #declaring a list 
    vowel = "aeiouAEIOU " #declaring the string of vowel and space
    const="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPRQSTVWXYZ" #declaring the string of consonant
    for f in str1:
        if f in const:#if consonant case
            x.append(f+'o'+f)
        elif f in vowel:#in vowel case
            x.append(f)
    print "".join(map(str,x))



str1= raw_input("enter any string")#taking string from user 
translate(str1)# calling function
