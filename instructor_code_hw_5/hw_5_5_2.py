def validate_datetime(user_input):
    """
    Validate teh input date string
    Return Values:
        True/False: Was the user input correct
        Tuple with date adn time values if input correct or
            String with error message if input false
    """

    date_time = user_input.split(" ")
    if len(date_time) != 2:
        return False, 'Format Invalid. Need separate date and time.'

    date_segment = date_time[0].split('/')
    if len(date_segment) != 3:
        return False, 'Date must have a month, day and ear, separated by a /'

    time_segment = date_time[1].split(':')
    if len(time_segment) != 3:
        return False, 'Time must have an hour, minute and second, separated a :'

    try:
        date_segment = [int(d) for d in date_segment]
    except:
        return False, 'Date segment must be all integers'
    try:
        time_segment = [int(d) for d in time_segment]
    except:
        return False, 'Time segment must be all integers'

    if not 1 <= date_segment[0] <= 12:  # month checker
        return False, 'Month must be from 1 to 12'
    if not 1 <= date_segment[1] <= 31:  # crude day checker
        return False, 'Days must be from 1 to 31'
    if not 2000 <= date_segment[2] <= 2100:
        return False, 'Year must be from 2000 to 2100'
    if not 0 <= time_segment[0] <= 23:
        return False, 'House must be from 0 to 59'
    if not 0 <= time_segment[1] <= 59:
        return False, 'Minute must be from 0 to 59'
    if not 0 <= time_segment[2] <= 59:
        return False, 'Second must be from 0 to 59'

    return True, (date_segment, time_segment)


if __name__ == "__main__":

    user_input = input('Enter date and tiem (24-hour clock) using '
                       '"MM/DD/YYYY HR:MIN:SEC" format: ')
    # validate input
    success, info = validate_datetime(user_input)

    if success:
        date_segment, time_segment = info
        print('a. DD/MM/YYYY: {:0>2d}/{:0>2d}/{:0>2d}'.format(
            date_segment[1], date_segment[0], date_segment[2]))

        print('b. HR:MIN:SEC: {:0>2d}:{:0>2d}:{:0>2d}'.format(
            time_segment[0], time_segment[1], time_segment[2]))

        print('c. MM/YYYY: {:0>2d}/{:0>2d}'.format(
            date_segment[0], date_segment[2]))

        print('d. The time of day is {} {}. '.format(time_segment[0], 'AM' if time_segment[0] < 12 else 'PM'))

    else:
        print(info)

    print('-' * 50)
