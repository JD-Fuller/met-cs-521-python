"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20 SEPT 2020
Homework Problem # 1
Description of Problem : User input and number verification from formula
"""

# get user input
# user input add 2, multiply by 3, subtract 6, divide by 3
# If input equals result, print "Success", else, does not match.

# Function performs the required logical formula on user provided number
def math_it(x):
    return (((x + 2) * 3) - 6) / 3


# Function verifies user input is an integer
def user_num(num):
    while True:
        try:
            usr_input = int(input(num))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        else:
            return usr_input


# Start program and gather user input
number = user_num("Please enter a number of your choice:")
param1 = math_it(number)

# Determines truth of user input compared to math_it
if param1 == number:
    print(" Your number matches the great oracle's number of " + str(int(param1)) + ", great fortune lies in your path.")
else:
    print("Your number does not match the oracle's number " + str(int(param1)) + ", dark roads ahead for you lie.")
