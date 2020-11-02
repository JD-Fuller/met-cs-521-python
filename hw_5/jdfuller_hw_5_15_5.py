"""
JD Fuller
Class: CS 521 - Fall 1
Date: 07OCT2020
Homework Problem # 5
Description of Problem: Calculate compound interest using two functions - one non-recursive, one recursive
"""
import re
import string


def calc_compound_interest(p, i, n):
    """
    Calculate Compound interest
    :type n: int
    :param p: int
    :param i: float
    :param n: int
    :return: float
    """
    return p * ((1 + i) ** n)


def calc_compound_interest_recursive(p, i, y):
    """
    Calculate compound interest using recursion
    :param y: years
    :param p: principal
    :param i: interest rate
    :return:
    """
    if y == 0:
        return p
    else:
        interest = p * i
        return calc_compound_interest_recursive(p + interest, i, y - 1)

# Validate inputs and call functions to calculate interest
while True:
    principal_input = input("Please enter principal amount: ")
    int_rate_input = input("Please enter interest rate (Ex: 1.5%, 10%, 3.2%): ")
    years_input = input("Please enter years of investment: ")
    try:
        # Clean and verify input
        principal = int(re.sub('[' + string.punctuation + ']', '', principal_input))
        int_rate = float(int_rate_input.rstrip('%')) / 100  # type: float
        years = int(re.sub('[' + string.punctuation + ']', '', years_input))
        # Assign test values to verify type
        a = principal  # type: int
        b = int_rate  # type: float
        c = years  # type: int
        # Check functionality
        a += 1
        x = b * 100
        c += 1

        result_1 = round(calc_compound_interest(principal, int_rate, years), 4)
        print("Compound Interest Calculation: ", "$"+'{:,.2f}'.format(result_1))
        result_2 = round(calc_compound_interest_recursive(principal, int_rate, years), 4)
        print("Compound Interest Recursive Calculation: ", "$"+'{:,.2f}'.format(result_2))
        # Result of comparison between two calculations
        if result_1 == result_2:
            print("Calculations are equal when rounded to four decimal places.")
        else:
            print("Calculations do not match when rounded to four decimal places.")
        follow_up = (input("Would you like to make another calculation? (Enter 'Y' for yes, 'N' for no)"))
        if follow_up == 'y':
            continue
        else:
            print("Thanks you and have a great day!")
            break
    # Error Handling section
    except TypeError:
        print("Invalid: Entry must be of type Integer.")
    except ValueError:
        print("Invalid Input: Use only integers and no alphabet characters")
    except AssertionError:
        print("Function was not executed. Try again.")
    except IndexError:
        print("Invalid Input: Values must be integers with no whitespace or punctuation.")
