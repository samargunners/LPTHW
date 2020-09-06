def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split()
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_words(words):
    """Prints thre first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_words(words):
    """Prints the last word agter popping it off """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_frist_words(words)
    print_last_words(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)
