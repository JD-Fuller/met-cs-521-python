"""
JD Fuller
Class: CS 521 - Fall 1
Date: 27SEPT2020
Homework Problem # 3
Description of Problem: Create program that interprets input string uppercase, lowercase, digits and punctuation - returns data

"""
import string

# User prompt for input
usr_input = input("Enter Phrase: ")


# Function parses out uppercase, lowercase, digits, and punctuation of user input
def parce_string(phrase):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    punctuation_count = 0
    for x in phrase:
        if x.isupper():
            upper_count += 1
        elif x.islower():
            lower_count += 1
        elif x.isdigit():
            digit_count += 1
        elif string.punctuation:
            punctuation_count += 1
        else:
            continue
    return upper_count, lower_count, digit_count, punctuation_count


# Invoke function and set variables for return arguments
u_case_cnt, l_case_cnt, digit_cnt, punct_cnt = parce_string(usr_input)

# Output formatted table with labels
user_table = [
    [
        '# Upper', '# Lower', '# Digits', '# Punct.'
    ],
    [
        '--------', '--------', '--------', '--------'
    ],
    [
        u_case_cnt, l_case_cnt, digit_cnt, punct_cnt
    ]
]
for row in user_table:
    print("{: ^10} {: ^10} {: ^10} {: ^10}".format(*row))
