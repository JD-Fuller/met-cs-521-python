"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20OCT2020
Final Project
Description of Problem: TimeLoggrReport handles outbound txt file and csv erasing"""
import csv
from csv import *
from datetime import *


class TimeLoggrReport(object):
    """TimeLoggrReport Class contains handling methods for writing data to txt file and deleting csv information"""

    def __init__(self, project):
        self.__created_date = datetime.now()
        assert isinstance(project, str)
        self.file_project_name = project

    def write_file(self):
        """Write logs to txt file"""
        project = self.file_project_name
        created_date = self.__created_date
        new_list = []
        with open('TimeLog.csv', 'r') as csv_file:
            line_reader = csv.reader(csv_file, delimiter=',')
            next(csv_file)
            for row in line_reader:
                new_list.append(row)

        with open("timeloggr_{}_{}.txt".format(str(project), (str(created_date))), "w+") as f:
            for item in new_list:
                f.write('%s\n' % item)
            f.close()
        print("Files now available as ", str(f.name))

    def kill_file(self):
        """Erases all data in CSV file and resets header to start logging fresh data"""
        header = ('Task', 'Time', 'Date')
        k_file = 'TimeLog.csv'
        f = open(k_file, "w+")
        header_writer = writer(f)
        header_writer.writerow(header)
