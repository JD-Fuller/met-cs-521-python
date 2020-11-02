"""
JD Fuller
Class: CS 521 - Fall 1
Date: 04OCT2020
Homework Problem # 5
Description of Problem: Given a string, return count of letters from string, determine max, print unique letters by count
"""
# Starting CONST for use throughout the program
SENTENCE = "One ring to rule them all"

# Remove whitespaces for parsing
parse_list = [item for item in SENTENCE.replace(" ", "")]


# Create dictionary of letters from SENTENCE with frequency as value
def count_string(user_list):
    # Dictionary to capture items in list and counts
    ltr_freq = {}
    for letter in user_list:
        if letter in ltr_freq:
            ltr_freq[letter] += 1
        else:
            ltr_freq[letter] = 1
    return ltr_freq


# Get list of keys with frequency
new_list = count_string(parse_list)


# Determine max values of letters within SENTENCE
def find_max_vals(dict_of_vals):
    # Gather max value
    max_dict_val = max(dict_of_vals.values())
    # Create list of keys with corresponding values
    max_value_list = [key for key, value in dict_of_vals.items() if value == max_dict_val]
    if len(max_value_list) != 1:
        print("\n2. Most frequent letters {ltrs} appear {nums} times".format(ltrs=str(max_value_list),
                                                                             nums=max_dict_val))
    else:
        print("\n2. Most frequent letter {ltrs} appears {nums} times".format(ltrs=str(max_value_list),
                                                                             nums=max_dict_val))


# Current Active string being utilized
print("The string being analyzed is: " + '"' + SENTENCE + '"')

# Gather sorted list and print
print("1. Sorted dictionary of letter counts: ", end="")
[print((x, new_list[x]), end=" ") for x in sorted(new_list)]

# Printout most frequent letters with count
find_max_vals(new_list)


# Return histogram list of letters from sentence
def histogram_creator(params):
    # For each key value pair in a dict, create a list
    histogram_list = []
    for key, value in params.items():
        histogram_list.append(key * value)
    print("3. Histogram:", *histogram_list, sep="\n")
    return histogram_list


histogram_creator(new_list)
