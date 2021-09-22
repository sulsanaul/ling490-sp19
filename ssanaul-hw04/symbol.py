class Symbol:
    
    def __init__(self, value):
        self.value = None if value is None else str(value)

    def __eq__(self, other):
        return (self.value == other.value) if isinstance(other, Symbol) else NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.value if self else '\u03b5'

    def __bool__(self):
        return self.value is not None

    def __len__(self):
        return len(str(self.value)) if self else 0

    def isEpsilon(self):
        return not self

    def isNonTerminal(self):
        if self.isEpsilon():
            return False
        initChar = self.value[0]
        return initChar.isupper()

    def isTerminal(self):
        return not self.isNonTerminal()
