"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20OCT2020
Final Project
Description of Class: TimeLoggSums returns sum of time for all tasks or single task name"""
from datetime import *
import csv


class TimeLoggSums(object):
    """Class TimeLoggSums handles all addition of sums for all tasks or single tasks"""
    def __init__(self):
        self.__created_date = datetime.now()
        self.__name = 'TimeLoggSum'

    def sum_by_task(self, name):
        """Returns sum of time by task name"""
        with open("TimeLog.csv", 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            total_hours = 0
            total_minutes = 0
            next(csv_file)  # Skip header row
            for row in reader:
                if row[0] == name:
                    task, task_time, day = row
                    hour, minute, secs = [int(task_time) for task_time in task_time.split(":")]
                    total_hours += hour
                    total_minutes += minute
                if total_minutes > 60:
                    (add_hr, total_minutes) = divmod(total_minutes, 60)
                    total_hours += add_hr
        print('Total "{0}" Task Time: Hrs = {1}  Mins = {2}'.format(str(name), str(total_hours), str(total_minutes)))

    def sum_all_tasks(self):
        """Returns time sum of all tasks, regardless of task name"""
        with open("TimeLog.csv", 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(csv_file)  # Skip header row
            total_hours = 0
            total_minutes = 0
            for row in reader:
                task, t_time, day = row
                hour, minute, secs = [int(t_time) for t_time in t_time.split(":")]
                total_hours += hour
                total_minutes += minute
            if total_minutes > 60:
                (add_hr, total_minutes) = divmod(total_minutes, 60)
                total_hours += add_hr
        print('All Tasks: Hrs = {0}  Mins = {1}'.format(str(total_hours), str(total_minutes)))
        # return 'All Tasks: Hrs = {0}  Mins = {1}'.format(str(total_hours), str(total_minutes))


    def __repr__(self):
        """Return class description"""
        return 'TimeLoggrSums: (%s, %s)' % (self.__name, self.__created_date)
