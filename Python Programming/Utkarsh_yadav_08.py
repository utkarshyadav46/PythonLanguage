alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
num=['1','2','3','4','5','6','7','8','9','0']
cno=0
cal=0
str1=raw_input("please enter your string ")
for n in str1:
    if n in num:
        cno=cno+1
    elif n in alp:
        cal=cal+1

print "Letters",cal
print "Digits",cno
        
