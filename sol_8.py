'''
This file contains the solution to the following question

8.Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.


'''

import random

# Generate a random 4-digit number consisting of 0s and 1s
num_str = "".join([random.choice(['0', '1']) for _ in range(4)])

# Convert the number to base 10
num_base_10 = int(num_str, 2)

# Print the results
print("Random number in base 2:", num_str)
print("Random number in base 10:", num_base_10)