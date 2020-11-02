def vc_cntr(sentence):
    """
    Return count of vowels and consonants from input sentence
    :param sentence:
    :return:
    """
    vowels = "AEIOU"

    sentence = sentence.upper()

    v_total = len([v for v in sentence if v in vowels])

    c_total = len([c for c in sentence if c.isalpha() and c not in vowels])

    return {'total_vowels': v_total,
            'total_consonants': c_total}


if __name__ == "__main__":
    user_input = input("Enter an English sentence: ")
    cnt_dict = vc_cntr(user_input)
    print("# vowels in sentence: {}".format(cnt_dict['total_vowels']))
    print("# consonants in sentence: {}".format(cnt_dict['total_consonants']))
