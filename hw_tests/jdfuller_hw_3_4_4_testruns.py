
#
#
# def sorted_list(user_integers):
#     while True:
#         try:
#             user_integers == input(sorted(user_integers))
#         except ValueError:
#             print("Error: The digits are not in ascending order. Please re-enter.")
#             continue
#         else:
#             return True


# sort_chk = check_for_integer(int_input)


# def three_digit(user_integers):
#     while True:
#         try:
#             len(user_integers) == 3
#         except ValueError:
#             print("Error: You did not enter a 3-digit number.")
#             continue
#         else:
#             return True


# digit_chk = check_for_integer(int_input)


# def duplicate_check(user_integers):
#     for x in user_integers:
#         if user_integers.count(x) > 1:
#             print('Error: Your Number contains duplication.')
#             continue
#         else:
#             return True


# dedup_chk = check_for_integer(int_input)


# def ultimate_check(user_integers):
#     x = user_integers
#     if checks_for_integer(x) and sorted_list(x) and duplicate_check(x) and three_digit(x):
#         print("Number Accepted!")
#     else:
#         SystemError("Your inputs have broken the system")


# def check_input(params):
#     x = input(params)
#     if checks_for_integer(x):
#         pass
#     else:
#         print("Error: This is not an integer. Please re-enter.")
#     if sorted_list(x):
#         pass
#     else:
#         print("Error: The digits are not in ascending order. Please re-enter.")
#     if len(x) == 3:
#         pass
#     else:
#         print("Error: You did nto enter a 3-digit number.")
#     if duplicate_check(x):
#         pass
#     else:
#         print('Error: Your Number contains duplication.')
#     if checks_for_integer(x) and sorted_list(x) and len(x) == 3 and duplicate_check(x):
#         print("Number accepted!")
# def check_input(params):
#     x_str = len(input(params))
#     if input(params).isdigit():
#         if params == input(sorted(params):
#             if x_str == 3:
#                 if duplicate_check(x):
#                     print("Number accepted")
#                 else:
#                     print('Error: Your Number contains duplication.')
#             else:
#                 print("Error: You did not enter a 3-digit number.")
#         else:
#             print("Error: The digits are not in ascending order. Please re-enter.")
#     else:
#         print("Error: This is not an integer. Please re-enter.")


# if checks_for_integer(x) and sorted_list(x) and len(x) == 3 and duplicate_check(x):
#     print("Number accepted!")


# int_input = input("Please enter a 3-digit integer: ")
# usr_input = input("Enter a number:")
# usr_list = list(usr_input)
# usr_int = int(usr_input)
# while True:
#     if not usr_input.isdigit():
#         print("Please type digits")
#         continue
#     else:
#         if len(usr_input) != 3:
#             print("Please, make length 3")
#             continue
#         else:
#             if usr_list != sorted(usr_list):
#                 print("Not in ascending order")
#                 continue
#             else:
#                 for x in usr_input:
#                     if usr_input.count(x) > 1:
#                         print('Error: Your Number contains duplication.')
#                         continue
#                     else:
#                         print("good to go")
#                         break

# while True:
#     if not usr_input.isdigit():
#         print("Please type digits")
#         continue
#     elif len(usr_input) != 3:
#         print("Please, make length 3")
#         continue
#     elif usr_list != sorted(usr_list):
#         print("Not in ascending order")
#         continue
#     elif usr_list[0] == usr_list[1] or usr_list[0] == usr_list[2] or usr_list[1] == usr_list[2]:
#         print('Error: Your Number contains duplication.')
#         continue
#     else:
#         print("good to go")
#         break

# while True:
#     usr_input = input("Enter a number:")
#     try:
#         usr_int = int(usr_input)
#     except ValueError:
#         if not usr_int.isdigit():
#             print("Please type digits")
#             continue
#
#         if len(usr_input) != 3:
#             print("Please, make length 3")
#             continue
#
#         if usr_list != sorted(usr_list):
#             print("Not in ascending order")
#             continue
#
#         if usr_list[0] == usr_list[1] or usr_list[0] == usr_list[2] or usr_list[1] == usr_list[2]:
#             print('Error: Your Number contains duplication.')
#             continue
#     else:
#         break
# print("good to go")

# input_len = len(int_input)
# sort_list = sorted(int_input)
# digit_check = int_input.isdigit()
# dedup_check = duplicate_check(int_input)
