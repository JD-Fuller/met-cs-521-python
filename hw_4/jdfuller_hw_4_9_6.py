"""
JD Fuller
Class: CS 521 - Fall 1
Date: 04OCT2020
Homework Problem # 6
Description of Problem: Prompt to input, validate the number, convert to words with dictionary
"""
import re

# Dictionary of key,value items for use
ltr_to_nums = {'Zero': '0', 'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5',
               'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9', 'Negative': '-', 'Point': '.'}


# Convert list to string and add separation
def convert_to_str(list_input, separator):
    output_str = separator.join(list_input)
    return output_str


# Gather user input and check against filter using REGEX
q = True
while q:
    user_input = str(input("Enter a number: "))

    # Create list to append each character of input into list
    usr_list = []
    for x in user_input:
        usr_list.append(x)

    # Check for letters and commas
    for x in usr_list:
        if re.search('[a-zA-Z]', user_input):
            print('"' + user_input + '"' + " is not a valid number. Please try again")
            break
            q = True

        if re.search(',+', user_input):
            print("Please try again without entering commas.")
            break
        else:
            # Append input that makes it through the filter into result list
            result = []
            for x in usr_list:
                for k, v in ltr_to_nums.items():
                    if v == x:
                        result.append(k)
                        # End loop
                        q = False

    # Print result list with spacing
    while not q:
        spacing = ' '
        text_printout = spacing.join(result)
        print("As Text: ", convert_to_str(result, spacing))
        q = True
