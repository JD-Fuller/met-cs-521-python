"""
JD Fuller
Class: CS 521 - Fall 1
Date: 04OCT2020
Homework Problem # 4
Description of Problem: Parse data out from dictionary - extract keys, values, key value pairs -> ordered by both key and value

"""
my_dict = {'a': 15, 'c': 18, 'b': 20}

# Gather list of keys from my_dict
key_list = [key for key in my_dict]
value_list = [value for value in my_dict.values()]

# Print Keys and Values Separately
print("Keys: " + str(key_list))
print("Values: " + str(value_list))

# Print Key Value Pairs
print("Key value pairs: ")
key_value_list = [print(key, ':', value) for key, value in my_dict.items()]

# Print Key Value pairs, ordered by key and value
print("Key value pairs ordered by key: " + str(sorted(my_dict.items())))
print("Key value pairs ordered by value: " + str(sorted(my_dict.items(), key=lambda x: x[1])))
