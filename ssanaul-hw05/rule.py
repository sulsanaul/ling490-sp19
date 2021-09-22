class Rule:

    def __init__(self, lhs, rhs):

        if isinstance(lhs, Symbol) and lhs.isNonTerminal():
            self.lhs = lhs
        else:
            raise RuntimeError("Error: Lhs must be a non-terminal Symbol object")

        if len(rhs) == 0:
            raise RuntimeError("Error: Rhs must have length greater than 0")
        else:
            for obj in rhs:
                if not isinstance(obj, Symbol):
                    raise RuntimeError("Error: Every element of rhs must be a Symbol object")
            self.rhs = rhs

    def __eq__(self, other):
        return str(self) == str(other) if isinstance(other, Rule) else NotImplemented

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        rhs_string = ''

        for obj in self.rhs:
            rhs_string += str(obj) + ' '

        return str(self.lhs) + ' \u2192 ' + rhs_string

    def __bool__(self):
        if len(self.rhs) == 1 and self.rhs[0].isEpsilon():
            return False
        else:
            return True

    def __len__(self):
        return len(self.rhs)

    @staticmethod
    def readLine(line):
        if line.isNonTerminal():
            return Rule(Symbol(line), [Symbol(None)])

        else:
            symbols    = line.split()[1:]
            lhs_symbol = symbols[0]
            rhs_list   = []

            for obj in symbols:
                rhs_list += Symbol(obj)

            return Rule(lhs_symbol, rhs_list)
