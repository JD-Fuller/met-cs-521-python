"""
JD Fuller
Class: CS 521 - Fall 1
Date: 04OCT2020
Homework Problem # 2
Description of Problem: Generate new list of numbers from list, such that new list is from sum of each neighbor
integer in old list
"""

# Constant list of integers
L = [10, 20, 30, 40, 50]

# Handle first two values in list
first_sum_list = [L[0] + L[1]]

# List Comprehension to cover all values between beginning and end of list
mid_sum_list = [((value-1) + value + (value+1)) for value in L[1:-1]]

# Handle last two values in list
last_sum_list = [L[-1] + L[-2]]

# Combine all three lists
final_list = first_sum_list + mid_sum_list + last_sum_list


print("Input List: " + str(L))
print("Result List: " + str(final_list))

