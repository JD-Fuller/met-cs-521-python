"""
JD Fuller
Class: CS 521 - Fall 1
Date: 04OCT2020
Homework Problem # 3
Description of Problem: Validate two lists for size, create a dictionary with keys of last name and value = first name
"""
# Two Constant lists

f_name = ['Jane', 'John', 'Jack']
l_name = ['Doe', 'Deer', 'Black']


# Function to check length of input lists, create dictionary of combined values
def dict_maker(l, f):
    # Check for equal length
    if len(l) != len(f):
        print("The two lists are not equal in length")
    else:
        # Combine two lists into dictionary with zip
        new_dict = dict(zip(l, f))
        return new_dict


print("First Names: " + str(f_name))
print("Last Names: " + str(l_name))
print("Name Dictionary: " + str(dict_maker(l_name, f_name)))
