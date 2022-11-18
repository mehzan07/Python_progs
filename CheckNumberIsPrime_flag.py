# Use global varible to check  a number is prime or not

numb= 29 # default value

# Ask from user to give a numbber
numb = int(input("Enter a numbber: "))

# define a bool variable which can be uppdated in the loop
isPrime = False

# prime numbbers are greater than 1
if numb > 1:
    # check for factors
    for i in range(2, numb):
        if (numb % i) == 0:
            # if factor is found, set flag to True
            isPrime = True
            # break out of loop
            break

# check the value of bool varis True
if isPrime:
    print(numb, "is not a prime number")
else:
    print(numb, "is a prime numer")