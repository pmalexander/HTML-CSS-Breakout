print ("FizzBuzz counting up to 100!")

b = 1
n = 150
fz = n % 3 == 0
bz = n % 5 == 0

#can't figure out if should use 'while' statement, unsure on how to set specific numbers to reflect divisible numbers

numbers = 1
increasing = True

while increasing:
    if (numbers <= n):
        print("{}".format(numbers))
        numbers #use? 
    else:
        increasing = False

#maybe 'for'?

for n in range(b, n):
    if (n % 3 == 0):
        print("Fizz")    

for n in range(b, n):
    if (n % 5 == 0):
        print("Buzz")    

for n in range(b, n):
    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")        


