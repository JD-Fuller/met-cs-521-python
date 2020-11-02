"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20OCT2020
Final Project
Description of Class: TimeLoggrTask sets task to csv and gets all tasks"""
import csv
from csv import writer
from datetime import *
from pprint import pprint
from TimeLoggSums import TimeLoggSums
from TimeLoggrMenu import Colors
from TimeLoggrReport import TimeLoggrReport


class TimeLoggrTask(object):
    time_sums = TimeLoggSums()
    """Collect time inputs of activities logged and returns summary report"""

    def __init__(self, project):
        self.__created_date = datetime.now()
        assert isinstance(project, str)
        self.project_name = project

    def set_task(self, task, time_spent, *args):
        """Writes single task to file"""
        __created_date = datetime.now()
        __project_parent = self.project_name
        assert isinstance(task, str)
        try:
            time_worked = datetime.strptime(time_spent, '%H:%M').time()
        except ValueError:
            print("Incorrect time format, validate hours and minutes input")
            return ValueError("Incorrect time format, should be HH:MM")

        if args:
            inp_date = ''.join(args)
            date_worked = datetime.strptime(inp_date, '%m/%d/%Y').date()
        else:
            date_worked = datetime.now().date()
        task_entry = [task, time_worked, date_worked]
        # Write true task to TimeLoggrTask.csv file
        with open('TimeLog.csv', 'a+', newline='') as csv_log:
            csv_writer = writer(csv_log)
            csv_writer.writerow(task_entry)
        print(Colors.FontColor.blue, task.capitalize() + ' task has been logged \u2713', Colors.reset)

    def get_tasks_by_name(self, name):
        """Returns tasks by query of task name"""
        assert isinstance(name, str)
        task_list = []
        with open('TimeLog.csv', 'r') as csv_file:
            line_reader = csv.reader(csv_file, delimiter=',')
            next(csv_file)
            for row in line_reader:
                if name == row[0]:
                    task_list.append(row)
        pprint('Report of Tasks:')
        pprint(task_list)
        pprint(time_sums.sum_by_task(name))

    def get_all_tasks(self):
        """Return all tasks for project"""
        all_tasks = []
        with open('TimeLog.csv', 'r') as csv_file:
            line_reader = csv.reader(csv_file, delimiter=',')
            next(csv_file)
            for row in line_reader:
                all_tasks.append(row)
        pprint('Report -- All Tasks:')
        pprint(all_tasks)
        pprint(time_sums.sum_all_tasks())

    # Call to repr() prints objects information
    def __repr__(self):
        return 'TimeLoggrTask: (%s, %s)' % (self.project_name, self.__created_date)


if __name__ != "__main__":
    time_sums = TimeLoggSums()

if __name__ == "__main__":
    # unit tests
    test_log = 'python-test'
    test_time = '01:30'

    test_tasklog = TimeLoggrTask('test-log-task')
    test_time_fn = TimeLoggSums()
    clear_log = TimeLoggrReport('test-set-task')
    clear_log.kill_file()
    test_tasklog.set_task(test_log, test_time)
    assert test_time_fn.sum_all_tasks() == 'All Tasks: Hrs = 1  Mins = 30', 'Assertion Error: Check Input'
    clear_log.kill_file()
    assert test_time_fn.sum_all_tasks() == 'All Tasks: Hrs = 0  Mins = 0', 'Assertion Error: Check Input'
    print("All tests passed")


