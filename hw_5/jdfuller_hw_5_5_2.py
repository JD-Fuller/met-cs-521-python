"""
JD Fuller
Class: CS 521 - Fall 1
Date: 07OCT2020
Homework Problem # 2
Description of Problem: Validate datetime input from user and return parsed out strings of input
"""
import re


class ValidationErrors(Exception):
    """Raised when input does not meet criteria of datetime.

    Attributes:
        message -- explanation of why the specific input failed.
    """
    message = ...  # type: str

    def __init__(self, message):
        """
        :type message: str
        """
        self.message = message


def is_valid_datetime(user_inp: str):
    """ Validate datetime input by user
    :param user_inp: str
    """
    while True:
        if not re.match('^[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}$', user_inp):
            raise ValidationErrors("Invalid: Format does not match required format.")
        # split user input on white space
        split_string_at_ws_internal = user_inp.split()
        # assign first item to date string
        date_split_internal = split_string_at_ws_internal[0].split('/')
        # assign second item to time string
        time_split_internal = split_string_at_ws_internal[1].split(':')
        # Filtering process to determine valid user input
        if not 1 <= int(date_split_internal[0]) <= 12:
            raise ValidationErrors("Invalid: Month not within the scope of available months")
        elif not 1 <= int(date_split_internal[1]) <= 31:
            raise ValidationErrors("Invalid: Day not within scope of available days.")
        elif not 1900 <= int(date_split_internal[2]) <= 2500:
            raise ValidationErrors("Invalid: Year not within scope of available years.")
        elif not 0 <= int(time_split_internal[0]) <= 23:
            raise ValidationErrors("Invalid: Hours out of scope of 24 hour day.")
        elif not 0 <= int(time_split_internal[1]) <= 59:
            raise ValidationErrors("Invalid: Minutes out of scope of 60 minutes range.")
        elif not 0 <= int(time_split_internal[2]) <= 59:
            raise ValidationErrors("Invalid: Seconds out of scope of 60 seconds range.")
        else:
            return True


# Loop through user input until validated from function
while True:
    try:
        user_input = input('Enter a date time (MM/DD/YYYY HR:MIN:SEC): ')
        is_valid_datetime(user_input)
        # split user input on white space
        split_string_at_ws = user_input.split()
        # assign first item to date string
        date_split = split_string_at_ws[0].split('/')
        # assign second item to time string
        time_split = split_string_at_ws[1].split(":")
        am_pm_set = ""
        if int(time_split[0]) >= 12:
            am_pm_set = "PM"
        else:
            am_pm_set = "AM"
        print('DD/MM/YYYY is {0}'.format(str(split_string_at_ws[0])))
        print('HR:MIN:SEC is {}:{}:{}'.format(time_split[0], time_split[1], time_split[2]))
        print('MM/YYYY is {0}/{1}'.format(date_split[0], date_split[2]))
        print('The time is {}'.format(am_pm_set))
        break
    except ValidationErrors as exception:
        print(exception.message)


