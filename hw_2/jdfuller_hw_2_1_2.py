"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20 SEPT 2020
Homework Problem # 2
Description of Problem : Input and types problem with verification of error creating input
"""

# gather user input and print input as str, int, and float


def print3times(params):

    print("This is an int:", int(params))
    print("This is a string:", str(params))
    print("This is a float:", float(params))


usr_input = input("Enter anything you'd like:")

print3times(usr_input)

"""
Be advised:
Without any error handling functionality added in, 
this program is unable to handle any type of input 
other than INT without generating an error.

In other words, if you enter an INT, you will not get an error. 
If you enter a string or float, you will get an error.
"""



