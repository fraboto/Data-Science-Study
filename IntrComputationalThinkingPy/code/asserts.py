def first_letter(word_list):
    first_letter_list = []

    try:
        for word in word_list:
            assert type(word) == str, f'{word} is not a string'
            assert len(word) > 0, 'Empty strings not allowed'

            first_letter_list.append(word[0])
    except AssertionError as e:
        print(e)

        return first_letter_list

word_list = ['abc', 5, '']
first_letter(word_list)