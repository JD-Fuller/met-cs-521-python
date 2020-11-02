"""
JD Fuller
Class: CS 521 - Fall 1
Date: 27SEPT2020
Homework Problem # 2
Description of Problem: Print statements based on odd string, based on length
"""

PHRASE = "I am the captain of my soul"


# Function counts string and determines if odd or even length - returns not odd if even == true
def count_string(phrase):
    count = 0
    for i in phrase:
        count += 1
        continue
    if count % 2 == 0:
        print("Not odd")
    else:
        return count


# Invokes Count String function and declares variable total string count
total_str_count = str(count_string(PHRASE))


# Function performs floor division to determine middle character of string and returns character
def middle_char(phrase):
    return phrase[(len(phrase) - 1) // 2]


# Invokes function and sets variable of middle character to char_str
mid_char_str = middle_char(PHRASE)
# Captures beginning of phrase, before middle of split without including middle digit
begin_phrase = str(PHRASE[0:(len(PHRASE) - 1) // 2])
# Captures end of phrase, after middle of split without including middle digit
end_phrase = str(PHRASE[(len(PHRASE) - 1) // 2 + 1:(len(PHRASE) + 1)])

print('My ' + total_str_count + ' character string is: ' + '"' + PHRASE + '"')
print('The middle character is: ' + '"' + mid_char_str + '"')
print('The 1st half of the string is: "' + begin_phrase + '"')
print('The 2nd half of the string is: "' + end_phrase + '"')
