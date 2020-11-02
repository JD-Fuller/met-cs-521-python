"""
JD Fuller
Class: CS 521 - Fall 1
Date: 27SEPT2020
Homework Problem # 1
Description of Problem: Count number of odd, even, squares, cubes of an integer range
"""
# Range of Numbers
N_MIN = 2
N_MAX = 130
num_list = list(range(N_MIN, N_MAX + 1))


# Function takes in list of integers, calculates odd and even integers, places them in separate list
def odd_or_even(num_range):
    inner_odd_num = 0
    inner_even_num = 0
    inner_even_list = []
    inner_odd_list = []
    for x in num_range:
        if x % 2 == 0:
            inner_even_num += 1
            inner_even_list.append(x)
        else:
            inner_odd_num += 1
            inner_odd_list.append(x)
    return inner_even_num, inner_odd_num, inner_even_list, inner_odd_list


# defining return values from function
even_num, odd_num, even_list, odd_list = odd_or_even(num_list)


# Function takes in range of numbers and max, returns count and list of squares within range
def squares_of_list(num_range, max_num):
    inner_square_list = []
    inner_square_count = 0
    for x in num_range:
        if (x ** 2) >= max_num:
            break
        else:
            inner_square_count += 1
            inner_square_list.append(x ** 2)
    return inner_square_count, inner_square_list


# Multiple outcomes of square function defined
square_count, square_list = squares_of_list(num_list, N_MAX)


# Function takes in range and max, returns total count and list of cubes within range
def cubes_of_list(num_range, max_num):
    inner_cube_list = []
    inner_cube_count = 0
    for x in num_range:
        if (x ** 3) >= max_num:
            break
        else:
            inner_cube_count += 1
            inner_cube_list.append(x ** 3)
    return inner_cube_count, inner_cube_list


# Multiple outputs from cubes function defined
cube_count, cube_list = cubes_of_list(num_list, N_MAX)

print("Checking numbers from " + str(N_MIN) + " to " + str(N_MAX))
print("Odd (" + str(odd_num) + "): " + str(odd_list[0]) + "..." + str(odd_list[-1]))
print("Even (" + str(even_num) + "): " + str(even_list[0]) + "..." + str(even_list[-1]))
print("Square (" + str(square_count) + "): " + str(square_list))
print("Cube (" + str(cube_count) + "): " + str(cube_list))
