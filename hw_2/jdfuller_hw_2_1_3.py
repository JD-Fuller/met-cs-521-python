"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20 SEPT 2020
Homework Problem # 3
Description of Problem : Input an integer and print value of formula, along with string of formula,
replacing 'n' for user input values.

"""


# Function to perform mathematical operation
def math_it(x):
    return x + x * x + x * x * x + x * x * x * x


# Function to handle invalid inputs
def user_num(num):
    while True:
        try:
            usr_input = int(input(num))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        else:
            return usr_input


# User input received
param = user_num("Enter a number:")


# Retrieve outcome of formula and convert to string
exp = str(math_it(param))


# Convert user input to string for use in concatenated string below
n = str(param)


# Concatenated string of outcome
print(str(n + "+" + n + "*" + n + "+" + n + "*" + n + "*" + n + "+" + n + "*" + n + "*" + n + "*" + n + "=" + exp))
