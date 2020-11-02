"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20 SEPT 2020
Homework Problem # 6
Description of Problem : Leap year calculation in 'for loop' and 'while loop'

"""

# Iterate through the range 1900 - 2021, for each increment of 4, print year
print("Leap Year with For Loop:")
for x in range(1900, 2021, 4):
    print(x)


# While the year count is less than 2021, print each year starting at 1900
print("\nLeap Year with While Loop:")
yearCount = 1900
while yearCount < 2021:
    print(yearCount)
    yearCount += 4
