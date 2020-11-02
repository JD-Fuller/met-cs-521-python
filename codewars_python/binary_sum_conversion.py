def add_binary(a, b):
    num = a + b
    print(bin(num).replace('0b', ''))
    return bin(num).replace('0b', '')


add_binary(10, 20)
add_binary(5, 5)
add_binary(6, 3)
