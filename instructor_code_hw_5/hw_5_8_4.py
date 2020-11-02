import sys


def list_to_once_words(inp_list):
    """ Generate a sublist of only unique words in input list"""

    word_dict = {}

    for e in inp_list:
        if e in word_dict:
            word_dict[e] += 1
        else:
            word_dict[e] = 1

    # return the unique list
    return sorted([k for k in word_dict if word_dict[k] == 1])


if __name__ == "__main__":

    my_file = input('What is the name of your word list text file: ')
    if my_file.strip() == '':
        my_file = 'words.txt'

    try:
        word_file = open(my_file, "r")
    except IOError as e:
        sys.exit('Error: File "{}" not found! Please try again.'.format(my_file))

    # read entire contents of the text file into one string
    file_data = ' '.join(word_file.readlines())

    # close the file
    word_file.close()

    # convert words to upper case and remove commas and periods.
    all_words = file_data.upper().replace('.', ' ').replace(',', ' ')

    # convert words to al ist based on spaces
    word_list = all_words.split()

    print('The following words occurred only once in the file: {}'.format(sorted(list_to_once_words(word_list))))
