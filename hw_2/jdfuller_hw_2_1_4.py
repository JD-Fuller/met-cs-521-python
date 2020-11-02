"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20 SEPT 2020
Homework Problem # 4
Description of Problem : Within 3 lines, gather input of user, convert input to int, print '0' if user input is even and
 '1' if user input is odd

"""

# Take user input and perform operation to determine remainder, print 1 or 0 dependent on ternary operation
usr_input = int(input("Enter a number:")) % 2
outcome = str(print(0)) if usr_input == 0 else str(print(1))
