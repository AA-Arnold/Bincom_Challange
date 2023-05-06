'''
This file contains the solution to the following question

7.BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.


'''

def recursive_search(lst, target):
    if not lst:
        return False
    if lst[0] == target:
        return True
    return recursive_search(lst[1:], target)

# Example usage:
numbers = [1, 5, 8, 9, 10, 12]
target_number = int(input("Enter a number to search: "))
if recursive_search(numbers, target_number):
    print(f"{target_number} was found in the list!")
else:
    print(f"{target_number} was not found in the list.")