"""
JD Fuller
Class: CS 521 - Fall 1
Date: 07OCT2020
Homework Problem # 4
Description of Problem: Prompt for filename, read and convert file words to list
"""
import os

# Determine path for txt files
# dir_name = os.getcwd()
# file_states = os.path.join(dir_name, 'jdfuller_hw_5_8_4.txt')

# Read words from txt file into list, splitting lines and words
result = []
with open('jdfuller_hw_5_8_4.txt', 'r') as words_list:
    for line in words_list:
        for word in line.split():
            result.append(word)
words_list.close()


def list_to_words(word_list: list) -> list:
    """
    Return list of words found once in the passed parameter list
    :type word_list: list
    :return: list
    """
    return_list = []  # type: List[Any]
    # Iterate through each word in the list and count occurrence
    for item in word_list:
        if word_list.count(item) == 1:
            # Append words with count of 1 to new list and return
            return_list.append(item)
    return return_list


print('List of words with only one occurrence in file: ', list_to_words(result))
