"""
JD Fuller
Class: CS 521 - Fall 1
Date: 27SEPT2020
Homework Problem # 6
Description of Problem: Read file line by line and store records in lists.
"""
import os

dir_name = os.getcwd()
file_stu = os.path.join(dir_name, 'jdfuller_hw_3_14_6_stu.txt')

# Open file with student data
students = open(file_stu, 'r')

# Create list of lists and add each line of student into list
student_list = []
for student in students:
    # Add each student line to list - removing \n from end of each line
    student_list.append(student.splitlines())

print(student_list)
students.close()
