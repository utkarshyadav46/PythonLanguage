#code challenge 15
for i in range(1,51): #iterating i from 1 to 50 
    if i%3==0 and i%5==0: #if i divisible by both 3 and 5
        print "FizzBuzz"
    elif i%5==0: #if i divisible by only 5
        print "Buzz"
    elif i%3==0: # if i divisible by only 3
        print "Fizz"
    else:       #or else for all number
        print i
        
