"""
JD Fuller
Class: CS 521 - Fall 1
Date: 07OCT2020
Homework Problem # 1
Description of Problem: Create a function that takes in string and returns dictionary count of vowels and consonants
"""

import re

user_input = input("Enter an English Sentence: ")

parse_list = re.sub('[^A-Za-z]+', '', user_input)

vowels = ['a', 'e', 'i', 'o', 'u']


def vc_counter(usr_string, check_list: list) -> dict:
    """
    Compute count of vowels and consonants within a string
    :param usr_string: string
    :type check_list: list
    """
    vowel_count = 0
    consonant_count = 0

    total_keys = ['total_vowels', 'total_consonants']
    for x in usr_string:
        if x in check_list:
            vowel_count += 1
        else:
            consonant_count += 1

    count = [vowel_count, consonant_count]
    count_dict = dict(zip(total_keys, count))
    return count_dict


result = vc_counter(parse_list, vowels)
total_vowels = result.get('total_vowels')
total_consonants = result.get('total_consonants')

print("Total # of vowels in sentence: ", total_vowels)
print("Total # of consonants in sentence: ", total_consonants)
