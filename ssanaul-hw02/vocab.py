class Vocabulary:

    def __init__(self):
        """Constructs a new empty Vocabulary object.

        This constructor initializes an empty dictionary called self.word2int,
           which can be used to map strings to integers.

        This constructor initializes an empty list called self.int2word,
           which can be used to map integers to strings.
        """
        self.word2int = dict()
        self.int2word = []


    def __iadd__(self, word):
        """Stores the string represented by word in this Vocabulary object.

        If word is not a string, this method raises a TypeError.

        If word is a string that has previously been stored in this Vocabulary object, 
           this method does nothing and returns self.

        Otherwise, let v = len(self)
           This method adds word as a key to self.word2int with value v,
           and appends word to the end of self.int2word,
           then returns self
        """
        if not isinstance(word, str):
            raise TypeError
        elif word in self.int2word:
            return self
        else:
            v = len(self)
            self.word2int[word] = v
            self.int2word.append(word)
            return self


    def __getitem__(self, key):
        """Enables a vocabulary object v to be accessed via the v[key] notation.
        
        If key is a string that has previously been added to this Vocabulary object,
           this method returns the integer value for that string.

        If key is a string that has not previously been added to this Vocabulary object,
           this method raises a KeyError.

        If key is an integer that has a corresponding string in the Vocabulary object,
           this method returns the corresponding string.

        If key is an integer that has no corresponding string in the Vocabulary object,
           this method raises an IndexError.

        Otherwise, this method raises a TypeError.
        """
        if isinstance(key, str):
            if key in self.word2int:
                return self.word2int[key]
            else:
                raise KeyError
        elif isinstance(key, int):
            if key >= 0 and key < len(self.int2word):
                return self.int2word[key]
            else:
                raise IndexError
        else:
            raise TypeError  


    def __len__(self):
        """Returns the number of words stored in this Vocabulary object."""
        return len(self.int2word)


    def __iter__(self):
        """Returns a new iterator object.

        The returned iterator should be capable of iterating
           over all of the strings stored in this Vocabulary object.

        The iteration order should be the same as that of self.int2word
        """
        return iter(self.int2word)

    def __contains__(self, item):
        """Returns whether the item passed in is stored in this Vocabulary object."""
        return item in self.word2int
