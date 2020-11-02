"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20OCT2020
Final Project
Description of Class: TimeLoggrApp acts as a controller of the entire TimeLoggr App
"""


class TimeLoggrMenu:
    """TimeLoggr Menu Provides printout data for the user at the start of the program and instructs on commands"""
    def __init__(self):
        print('\n')
        print(Colors.FontColor.blue, Colors.bold, 'TimeLoggr', Colors.reset)
        print('-' * 50)
        print(Colors.bold, "TimeLoggr is a digital punch clock to help you log hours worked, rested, or lunched!",
              Colors.reset, '\n')
        print("---> TimeLogging should adhere to the following format:\n"
              , Colors.FontColor.lightblue, "Enter -> 1.command -> 2.task/activity name -> 3.quantity of time -> 4.date"
                                            '\n', Colors.reset)

        print("Optionally, you can leave the date blank and TimeLoggr will use the current day as the default date." '\n')
        print("All available commands for input:")
        print("="*40, '\n')
        print(Colors.FontColor.green, "Log Task:", Colors.reset)
        print("-" * 20)
        print("     To log a task, type 'log', followed by the 'task-name' + 'time' + 'date'\n"
              , Colors.FontColor.yellow, "         EXAMPLE ====> 'log coding 01:30 12/20/2021'\n", Colors.reset)
        print(Colors.FontColor.cyan, "Reports:", Colors.reset)
        print("-" * 20)
        print("     Type 'report all' for a printout table of all tasks && sums\n"
              "     Type 'report {task-name}' for a printout of specific tasks && sums\n"
              , Colors.FontColor.yellow, "         EXAMPLE ====> report python", Colors.reset, "\n"
              "     Type 'report sum' for a sum report only of all time logged\n"
              "     Type 'report sum {task name}' for sum only report of a specific task\n"
              , Colors.FontColor.yellow, "         EXAMPLE ====> report sum python\n", Colors.reset,
              )
        print(Colors.FontColor.lightgreen, "Miscellaneous:", Colors.reset)
        print("-" * 20)
        print("     Type 'help' at anytime for a printout of the option menu\n"
              "     Type 'loggit' to send all logged items to a TXT file\n"
              "     Type 'cleanlogg' to erase all active logs\n"
              "     Type 'quit' at anytime to exit TimeLoggr\n")

    @staticmethod
    def info_menu():
        print("All available commands for input: \n")
        print("Type 'log' task-name time date => 'log coding 01:30 12/20/2021' to log a task"
              "Type 'report all' for a printout table of all tasks \n"
              "Type 'report {insert name of task}' for a printout of specific tasks\n"
              "Type 'report sum' for a sum of all time logged\n"
              "Type 'help' for a printout of the option menu\n"
              "Type 'loggit' to send logs to a TXT file\n"
              "Type 'cleanlogg' to erase all active logs\n"
              "Type 'quit' at anytime to exit TimeLoggr")


class Colors:
    """Colors Class/subclass fontcolor permits the use of terminal colors in the Timeloggr App"""
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class FontColor:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
