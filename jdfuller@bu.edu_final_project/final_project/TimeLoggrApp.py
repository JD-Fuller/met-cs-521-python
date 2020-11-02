"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20OCT2020
Final Project
Description of Class: TimeLoggrApp handles input control & error handling of the TimeLoggr application
"""
from TimeLoggrTask import TimeLoggrTask
from TimeLoggrMenu import TimeLoggrMenu
from TimeLoggrReport import TimeLoggrReport
from TimeLoggSums import TimeLoggSums
from TimeLoggrMenu import Colors
import re

if __name__ == '__main__':
    active_log = TimeLoggrTask('TimeLoggr')
    menu_screen = TimeLoggrMenu()
    time_sums = TimeLoggSums()

    while True:
        # User input - cleans and handles whitespace and punctuation
        user_input = re.sub(r'[^a-zA-Z0-9\d] +', ' ', str(input("Enter command: "))).strip()
        try:
            # Clean and verify input
            clean_string = [x for x in user_input.split(' ')]
            if len(clean_string) == 1:
                assert isinstance(clean_string[0], str), 'Invalid input for action - use log or report'
                if clean_string[0] == 'help':
                    print(menu_screen.info_menu())

                if clean_string[0] == 'quit':
                    print("TimeLoggr Out!")
                    break

                if clean_string[0] == 'loggit':
                    usr_input = input('What shall we call your logg? ')
                    log_report = TimeLoggrReport(str(usr_input))
                    log_report.write_file()
                    print(Colors.FontColor.blue, "Your data has been logg'd", Colors.reset)

                if clean_string[0] == 'cleanlogg':
                    usr_input = input('Are you sure? Type "y" for yes, or any key for no ')
                    if usr_input == 'y':
                        clean_csv = TimeLoggrReport(str(usr_input))
                        clean_csv.kill_file()
                        print("We were never here...")
                    else:
                        print('Phew! That was a close one.')

            # Conditionals for commands
            elif len(clean_string) > 1:
                assert isinstance(clean_string[1], str), 'Invalid input: Try again'
                assert (clean_string[1]), 'Task required for input'
                assert 1 <= len(clean_string) <= 4, 'Verify correct spacing of input'
                if clean_string[0] == 'report':
                    if clean_string[1] == 'all':
                        active_log.get_all_tasks()
                    elif clean_string[1] == 'sum' and len(clean_string) == 2:
                        time_sums.sum_all_tasks()
                    elif clean_string[1] == 'sum' and len(clean_string) == 3:
                        time_sums.sum_by_task(clean_string[2])
                    elif clean_string[1]:
                        active_log.get_tasks_by_name(clean_string[1])
                    else:
                        print("Try input again. Task not able to be entered.")
                elif clean_string[0] == 'log':
                    if len(clean_string) == 4:
                        active_log.set_task(clean_string[1], clean_string[2], str(clean_string[3]))
                    else:
                        active_log.set_task(clean_string[1], clean_string[2])
            else:
                print("Invalid Input: Enter 'help' to see all options for input")

        # Error Handling section
        except TypeError:
            print("Invalid: Verify help items to determine proper input.")
        except ValueError:
            print("Invalid Input: Check input for proper formatting")
        except AssertionError:
            print("Function was not executed. Check input against help menu and try again.")
        except IndexError:
            print("Invalid Input: Missing required inputs. See required input and try again.")
