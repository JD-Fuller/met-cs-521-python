"""


x_str = "Boston University"

for x in x_str:
    x_int = ord(x)
    print(x_int, end=" ")


x_list = [90, 80, 110, 270]
for x in x_list:
    x_char = chr(x)
    print("value: ", x, "character: ", x_char)

"""

# x_list = range(2, 131)
# for x in x_list:
#     x_char = chr(x)
#     print('value: ', x, 'character: ', x_char)
#
# vowels = 'aeoiuy'
# x_str = 'apple'
#
# for e in x_str:
#     if e in vowels:
#         print(e)


VOWELS = 'aeoiuy'
x_str = """after
meat
comes
mustard"""

for i, e in enumerate(x_str):
    if e not in VOWELS and e != '\n':
        print(i, e)

for i, e in enumerate(x_str):
    e = x_str[i]
    if e in VOWELS:
        print(e, i)

for i in range(len(x_str)):
    e = x_str[i]
    if e not in VOWELS and e != '\n':
        print(i, e)


n = 10
x_list = list(range(2, 2*n+1, 2))

sum = 0
for e in range(2, 2*n+1, 2):
    sum += e
    print(sum)
print(sum)
