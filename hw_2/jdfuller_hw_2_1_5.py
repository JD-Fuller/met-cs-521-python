"""
JD Fuller
Class: CS 521 - Fall 1
Date: 20 SEPT 2020
Homework Problem # 5
Description of Problem : Calculate BMI of user in metric or imperial units with height and weight inputs

"""

# Take two inputs and perform BMI Formula

# Formula for BMI
import sys
import time


def bmi_formula(w, h, r) -> int:
    if r == str("M"):
        return w / h ** 2
    else:
        return 703 * w / h ** 2


# Gather input for Metric or Imperial
res = input("Would you like to utilize metric or imperial measurements? Type [I] for Imperial and [M] for Metric: ")

# Dependent upon user input, input request verbiage is altered.
if res == str("m"):
    height, weight = [int(height) for height in
                      input("For BMI printout, please enter height in meters and weight in kilograms, separated by a "
                            "space: \n").split()]
elif res == str("i"):
    height, weight = [int(height) for height in
                      input("For BMI printout, please enter height in inches and weight in pounds, separated by a "
                            "space: \n").split()]
else:
    print("That is not a valid input. Goodbye.")
    raise SystemExit


bmi = bmi_formula(weight, height, res)
calculating_text = "Calculating BMI"
slow_text = "...... \n"
print_bmi = "\nPrinting BMI"
print(calculating_text)
for char in slow_text:
    sys.stdout.write("..")
    sys.stdout.flush()
    time.sleep(.4)
print(print_bmi)
for char in slow_text:
    sys.stdout.write("..")
    sys.stdout.flush()
    time.sleep(.4)

print("\nYour calculated BMI is ", round(bmi, 2))
