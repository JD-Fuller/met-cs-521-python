"""
Marc Lowenthal
Class: CS 521
Date:
Example using Mug.py
"""

from Mug import Mug

if __name__ == '__main__':

    # instantiate mug object
    marc_mug = Mug('clear', contents='beer',  material='glass')

    # set temperature
    marc_mug.set_temp(50)

    marc_mug.set_as_celsius()

    print(marc_mug)

    # Convert the result to a string,
    # get the length of the string, find the integer of 1/2 the length and
    # finally, multiply it by a two character line.
    print('=-' * int(round(len(str(marc_mug))/2,0)))


