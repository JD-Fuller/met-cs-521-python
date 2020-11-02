def duplicate_encode(word):
    working_word = word.lower()
    single_item = '('
    double_item = ')'
    new_string = []
    separator = ''
    for l in working_word:
        if working_word.count(l) > 1:
            new_string.append(double_item)
        else:
            new_string.append(single_item)
    print(separator.join(new_string))
    return separator.join(new_string)


# word = input('Enter word: ')
# duplicate_encode(word)
duplicate_encode('recede')
duplicate_encode('HPPbvezITdla IxGlcOOb')
duplicate_encode('Success')
