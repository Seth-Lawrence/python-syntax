list_of_words = ["hello", "hey", "goodbye", "yo", "yes","ease","Elephant"]
must_start_with={"h", "y"}


def make_uppercase(word_list):
    """takes a list of words, prints out each word in all uppercase"""
    for word in word_list:
        # print(word)
        print(word.upper())

# make_uppercase(list_of_words)



def print_words_staring_with_e(word_list):
    """takes a list of words, prints out each word that start with e"""
    for word in word_list:
        if (word.startswith('e') or word.startswith('E')):
            print(word)

# make_uppercase(list_of_words)

# print_words_staring_with_e(list_of_words)


def print_words(word_list,letter_list):
    for word in word_list:
        if (letter_list.__contains__(word[0])):
            print(word)

print_words(list_of_words, must_start_with)




