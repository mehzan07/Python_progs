# check  a input numbber is prime or not

numb = 407  # default value

# To take input from the user

numb = int(input("Enter a numbber: "))

# if numb >1
if numb > 1:
   # find the f irst factor
   for i in range(2,numb):
       if (numb % i) == 0: # if reminder is 0 (devidble)
           print(numb,"is not a prime numbber")
           print(i,"times",numb//i,"is",numb)
           break
   else:
       print(numb,"is a prime numbber")
       
# In case input numbber is less than or equal to 1, it is not prime
else:
   print(numb,"is not a prime numbber")