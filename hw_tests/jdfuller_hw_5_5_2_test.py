"""
JD Fuller
Class: CS 521 - Fall 1
Date: 07OCT2020
Homework Problem # 2
Description of Problem: Take in DateTime from user and verify if valid according to predetermined business logic
"""
import re


def is_valid_datetime(user_inp):
    """ Validate datetime input by user """
    if re.match('^[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}$', user_inp):
        pass
    else:
        return 'Invalid: Input does not match required format'
    # split user input on white space
    split_string_at_ws_internal = user_inp.split()
    # assign first item to date string
    date_split_internal = split_string_at_ws_internal[0].split('/')
    # assign second item to time string
    time_split_internal = split_string_at_ws_internal[1].split(':')
    # Filtering process to determine valid user input
    if 1 <= int(date_split_internal[0]) <= 12:
        if 1 <= int(date_split_internal[1]) <= 31:
            if 1900 <= int(date_split_internal[2]) <= 2500:
                if 0 <= int(time_split_internal[0]) <= 23:
                    if 0 <= int(time_split_internal[1]) <= 59:
                        if 0 <= int(time_split_internal[2]) <= 59:
                            return True
                        else:
                            return 'Invalid: Seconds are out of scope for viable seconds.'
                    else:
                        return 'Invalid: Minutes are out of scope for viable minutes.'
                else:
                    return 'Invalid: Hours are out of scope for viable minutes.'
            else:
                return 'Invalid: Year does not fit parameters of valid year'
        else:
            return 'Invalid: The day entered is not within the scope of possible days'
    else:
        return 'Invalid: The month entered is not within scope of possible months'


user_input = input('Enter a date time (MM/DD/YYYY HR:MIN:SEC): ')


if is_valid_datetime(user_input):
    # split user input on white space
    split_string_at_ws = user_input.split()
    # assign first item to date string
    date_split = split_string_at_ws[0].split('/')
    print(date_split)
    # assign second item to time string
    time_split = split_string_at_ws[1].split(":")
    print(time_split)
    am_pm_set = ""
    if int(time_split[0]) >= 12:
        am_pm_set = "PM"
    else:
        am_pm_set = "AM"
    print('DD/MM/YYYY is {0}'.format(str(split_string_at_ws[0])))
    print('HR:MIN:SEC is {}:{}:{}'.format(time_split[0], time_split[1], time_split[2]))
    print('MM/YYYY is {0}/{1}'.format(date_split[1], date_split[2]))
    print('The time is {}'.format(am_pm_set))
else:
    print(is_valid_datetime(user_input))

# user_input = "12/13/2020 11:31:24"
# invalid_date_m = "14/13/2020 11:31:24"
# invalid_date_d = "12/49/2020 11:31:25"
# invalid_date_y = "12/12/1890 11:31:25"
# invalid_time_h = "12/12/2020 39:31:25"
# invalid_time_m = "12/12/2020 23:78:25"
# invalid_time_s = "12/12/2020 23:30:99"
# invalid_format_1 = "122/12/2020 23:30:15"
# invalid_format_2 = "12/122/2020 23:30:15"
# invalid_format_3 = "12/12/20201 23:30:15"

# is_valid_datetime(user_input)
# is_valid_datetime(invalid_date_m)
# is_valid_datetime(invalid_date_d)
# is_valid_datetime(invalid_date_y)
# is_valid_datetime(invalid_time_h)
# is_valid_datetime(invalid_time_m)
# is_valid_datetime(invalid_time_s)
# is_valid_datetime(invalid_format_1)
# is_valid_datetime(invalid_format_2)
# is_valid_datetime(invalid_format_3)
