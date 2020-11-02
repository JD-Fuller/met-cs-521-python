"""
JD Fuller
Class: CS 521 - Fall 1
Date: 14OCT2020
Homework Problem # 1
Description of Problem: Create Class with class methods that performs alterations to string input
"""


class Sentence(object):
    """Sentence class takes in sentence of strings and returns alterations of strings"""
    def __init__(self, sentence='', list_index=0, new_word=''):
        self.__original_sentence = sentence
        assert isinstance(sentence, str), 'Sentence is not string.'
        self.__str_as_list = []
        self.selected_word = list_index
        self.replacement_word = new_word

    def __str__(self):
        return 'Sentence is "{}"'.format(self.__original_sentence)

    def get_all_words(self) -> object:
        """Return all words from original sentence string in a list"""
        for word in self.__original_sentence.split():
            self.__str_as_list.append(word)
        return self.__str_as_list

    def get_word(self, list_index):
        """Return word at specific index in original sentence string"""
        assert isinstance(list_index, int), 'Number required for input'
        assert 0 <= int(list_index) <= len(self.__str_as_list), 'Input out of scope of sentence length.'
        return self.__str_as_list[list_index]

    def set_word(self, list_index, new_word):
        """Take in new word and insert into sentence at specific index"""
        assert isinstance(new_word, str), 'String not entered for new word.'
        assert isinstance(list_index, int), 'Number required for index.'
        self.__str_as_list[list_index] = new_word
        self.__original_sentence = ' '.join(self.__str_as_list)


# Unit Tests
if __name__ == "__main__":
    sent_1 = 'Papa was a rolling stone'
    word_1 = 'stone'
    word_2 = 'pebble'
    index_1 = 4
    list_1 = ['Papa', 'was', 'a', 'rolling', 'stone']
    list_2 = ['Papa', 'was', 'a', 'rolling', 'pebble']

    # instantiate Sentence object
    jd_sentence = Sentence(sent_1, index_1, word_2)

    # Assert tests
    assert jd_sentence.get_all_words() == list_1, (
        'Error matching list {} != {}'.format(jd_sentence.get_all_words(), list_1))
    assert jd_sentence.get_word(index_1) == word_1, (
        'Error matching word {} != {}'.format(jd_sentence.get_word(index_1), word_1))
    jd_sentence.set_word(index_1, word_2)
    assert list_1 != jd_sentence.set_word(index_1, word_2), (
        'Error matching items {} != {}'.format(list_1, jd_sentence.set_word(index_1, word_2))
    )

    print(jd_sentence)
    jd_sentence.set_word(4, 'rock')
    print(jd_sentence)

    print('All tests passed')

