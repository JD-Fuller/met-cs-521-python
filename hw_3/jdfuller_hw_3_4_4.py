"""
JD Fuller
Class: CS 521 - Fall 1
Date: 27SEPT2020
Homework Problem # 4
Description of Problem: Gather user input and ensure input is digits in ascending order without duplicates
"""

# While loop prompts input until valid 3-digit input meets validation criteria
while True:
    usr_input = input("Please enter a 3-digit integer: ")

    # Create list to append each character of input into list
    usr_list = []
    for x in usr_input:
        usr_list.append(x)

    # Check to determine input is not integer
    if not usr_input.isdigit():
        print("Error: This is not an integer. Please re-enter.")
        continue

    # Check to determine if input meets length criteria of 3-digits
    if len(usr_list) < 3 or len(usr_list) > 3:
        print("Error: You did not enter a 3-digit number.")
        continue

    # Check to determine if duplicates are found between 3-digits
    if usr_list[0] == usr_list[1] or usr_list[0] == usr_list[2] or usr_list[1] == usr_list[2]:
        print("Your number contains duplication.")
        continue

    # Check to determine if list is in ascending order
    if usr_list != sorted(usr_list):
        print("Error: The digits are not in ascending order.")
        continue

    # If not true for all if statements, execute final printout
    else:
        break
print("Number Accepted!")
