class Symbol:
    
    def __init__(self, value):
        self.value = None if value is None else str(value)

    def __eq__(self, other):
        return (self.value == other.value) if isinstance(other, Symbol) else NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return '\u03b5' if self.value is None else self.value

    def __bool__(self):
        return not self.value is None

    def __len__(self):
        return 0 if self.value is None else len(self.value)

    def isEpsilon(self):
        return self.value is None

    def isNonTerminal(self):
        if self.isEpsilon():
            return False
        initChar = self.value[0]
        return initChar.isupper()

    def isTerminal(self):
        if self.isEpsilon():
            return False
        initChar = self.value[0]
        return not initChar.isupper()
