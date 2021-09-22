#!/usr/bin/python3

import sys
from vocab import Vocabulary
from min_edit_distance import min_edit_distance


def construct_vocabulary(vocab_file):
    """Given a whitespace-delimited text file (such as /usr/share/dict/words), 
    construct and return a Vocabulary object 
    that contains all of the words from the file.
    """
    v = Vocabulary()
    print("Constructing vocabulary...")
    with open(vocab_file, 'r') as f:
        for w in f.read().split():
            v += w
    print("Finished constructing vocabulary.")
    return v


def check_spelling(word, vocab):
    """Given a word and a vocabulary, 
    return the word from the vocabulary that is closest to the provided word.

    If the word is in the vocabulary, 
       then the word should be returned.

    If the word is not in the vocabulary, 
       this method should iterate through all items in the vocabulary.

       For every vocabulary item, compute the minimum edit distance.

       Return the vocabulary item with the lowest minimum edit distance.

       If two or more vocabulary items are tied for the lowest minimum edit distance,
          return the first such vocabulary item (the one with the lowest integer ID in the vocabulary).
    """
    if word in vocab:
        return word

    else:
        lowest_MED = min_edit_distance(word, vocab[0])
        closest_word_index = 0
        for i in range(1, len(vocab)):
            MED = min_edit_distance(word, vocab[i]) 
            if MED < lowest_MED:
                lowest_MED = MED
                closest_word_index = i
        return vocab[closest_word_index]

if __name__ == "__main__":

    # If this program is called with no arguments,
    #    call construct_vocabulary with /usr/share/dict/words,
    #    and read words from standard input.
    #
    # If this program is called with one arguments,
    #    treat the argument as the filename of a whitespace-delimited file,
    #    and read words from the file,
    #    and call construct_vocabulary with /usr/share/dict/words
    #
    # If this program is called with two arguments,
    #    treat the first argument as the filename of a whitespace-delimited file,
    #    and read words from that file,
    #    treat the second argument as the filename of a whitespace-delimited file,
    #    and call construct_vocabulary on that file
    #
    # Iterate over the provided words 
    #    (from standard input or from the user-provided file of possibly misspelled words).
    #
    # For every word, call check_spelling, and print the returned result to standard output
    
    if len(sys.argv) == 1:
        v = construct_vocabulary("/usr/share/dict/words")
        for w in sys.stdin.read().split():
            print("Suggested:", check_spelling(w,v))

    elif len(sys.argv) == 2:
        v = construct_vocabulary("/usr/share/dict/words")
        with open(sys.argv[1], 'r') as f:
            for w in f.read().split():
                print("Suggested:", check_spelling(w,v))

    elif len(sys.argv) == 3:
        v = construct_vocabulary(sys.argv[2])
        with open(sys.argv[1], 'r') as f:
            for w in f.read().split():
                print("Suggested:", check_spelling(w,v))
