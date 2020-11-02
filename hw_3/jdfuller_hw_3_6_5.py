"""
JD Fuller
Class: CS 521 - Fall 1
Date: 27SEPT2020
Homework Problem # 5
Description of Problem: Create test file with string rules and error messages for use of file
"""
import os

# Determine path for txt files
dir_name = os.getcwd()
file_y = os.path.join(dir_name, 'jdfuller_hw_3_6_5.txt')
file_x = os.path.join(dir_name, 'jdfuller_hw_3_6_5.new.txt')

line = 'Leonardo da Vinci !!'

# Create test file with single sentence of 20 words
text_file = open(file_y, 'w+')
text_file.write(line + '\n')
text_file.close()

# Read 4 lines of 5 words from test file
text_file = open(file_y, 'r')
result = text_file.read(5)
text_file.close()

# Write list of 4 lines into new test file
result_list = [(result + '\n') * 4]
new_file = open(file_x, 'w+')
for i in result_list:
    new_file.write(str(i))
new_file.close()

# Verify each line in test file only has 20 words and print error message if exceeds 20 words
new_file = open(file_x, 'r')
for new_line in new_file:
    # Combine lines to not count whitespace in error check
    new_line = new_line.strip(os.linesep)
    line_data = new_file.read().replace(" ", "")
    num_chars = len(line_data)

# Logic and Error Handling for 20 word max length check
while True:
    if len(line_data) > 20:
        print("Error: Lines should not exceed 20 letters.")
        break
    else:
        new_file.close()

    if os.path.isfile(file_x):
        print("File Exists")
        break
    else:
        print('File does not exist')
new_file.close()
