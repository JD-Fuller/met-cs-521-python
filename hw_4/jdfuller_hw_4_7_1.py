"""
JD Fuller
Class: CS 521 - Fall 1
Date: 04OCT2020
Homework Problem # 1
Description of Problem: Determine and print Odd & Even integers from list using list comprehension
"""

# Constant list of integers
L = range(1, 11)


# List comprehension determines evaluation_num == full list of integers in list
evaluation_num = [value for value in L]

# List comprehension extracts sum of even values in constant
even_sum = sum([value for value in L if value % 2 == 0])

# List comprehension extracts sum of odd values in constant
odd_sum = sum([value for value in L if value % 2 != 0])


print("Evaluating the numbers in: " + str(evaluation_num)[1:-1])
print("Even: " + str(even_sum))
print("Odd: " + str(odd_sum))
