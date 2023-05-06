'''
This file contains the solution to the following question

9.Write a program to sum the first 50 fibonacci sequence.


'''


# initialize variables
n1 = 0
n2 = 1
sum = 0

# loop to calculate the first 50 Fibonacci numbers
for i in range(50):
    sum += n1
    nth = n1 + n2
    n1 = n2
    n2 = nth

print("The sum of the first 50 Fibonacci numbers is:", sum)
