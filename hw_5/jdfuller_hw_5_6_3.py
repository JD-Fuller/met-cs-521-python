"""
JD Fuller
Class: CS 521 - Fall 1
Date: 07OCT2020
Homework Problem # 3
Description of Problem: Accept three inputs from user, validate inputs, perform logic to divide and add inputs
"""
import re


def calc_formula(usr_input: str):
    """
    Function calculates a/b + c
    :param usr_input: str
    """
    # split out input string for calculation
    str_parse_at_ws = usr_input.split()
    a = int(str_parse_at_ws[0])
    b = int(str_parse_at_ws[1])
    c = int(str_parse_at_ws[2])
    # Calculate results of parsed string, converted to integer
    result = a / b + c
    print('Formula: {}/{}+{}'.format(a, b, c),
          'Result: {}'.format(float(result)))
    return result


# Loop through user input until viable input is sent to calculation function
while True:
    user_input = input("Please enter three digits of any length, separated by a space (Example -> '124 32 8'): ")
    try:
        # Split out input for individual verification
        re.match('^[0-9]+ [0-9]+ [0-9]+', user_input)
        split_input_at_ws = user_input.split()
        a = int(split_input_at_ws[0])  # type: int
        b = int(split_input_at_ws[1])  # type: int
        c = int(split_input_at_ws[2])  # type: int
        a += 1
        x = 1/b
        c += 1
        calc_formula(user_input)
    # Error Handling section
    except ZeroDivisionError:
        print("Invalid: Second parameter cannot be zero.")

    except TypeError:
        print("Invalid: Entry must be of type Integer.")

    except ValueError:
        print("Invalid Input: Use only integers separated by whitespace.")

    except AssertionError:
        print("Function was not executed. Try again.")

    except IndexError:
        print("Invalid Input: Values must be integers separated by whitespace.")

