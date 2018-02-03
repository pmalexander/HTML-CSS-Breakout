print ("FizzBuzz counting up to 150!")

b = 1
n = 150

for o in range (b, n+1):
    
    if (o % 3 == 0) and (o % 5 == 0):
        print("FizzBuzz")        
        
    elif (o % 3 == 0):
        print("Fizz")    
        
    elif (o % 5 == 0):
        print("Buzz")
        
    else:
        print (o) 

print ("Complete!") 


    