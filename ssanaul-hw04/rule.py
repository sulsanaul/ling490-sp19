from symbol import Symbol

class Rule:

    def __init__(self, lhs, rhs):

        if not lhs.isNonTerminal():
            raise RuntimeError("Error: Lhs must be a non-terminal Symbol object")

        if len(rhs) < 1:
            raise RuntimeError("Error: Rhs must have length greater than 0")
        self.lhs = lhs
        self.rhs = rhs

    def __eq__(self, other):
        return str(self) == str(other) if isinstance(other, Rule) else NotImplemented

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        rhs_string = ''

        for obj in self.rhs:
            rhs_string += str(obj) + ' '

        return str(self.lhs) + ' --> ' + rhs_string
        #I was getting a unicode encoding error for '→' 
    def __bool__(self):
        return False if len(self.rhs) == 1 and self.rhs[0].isEpsilon() else True

    def __len__(self):
        return len(self.rhs) if self else 0

    @staticmethod
    def readLine(line):
        components = line.split()
        lhs_symbol = Symbol(components[0])
        if len(components) > 1:
            symbols  = components[1:]
            rhs_list = []

            for obj in symbols:
                rhs_list.append(Symbol(obj))

            return Rule(lhs_symbol, rhs_list)
        else:
            return Rule(lhs_symbol, [Symbol(None)])
