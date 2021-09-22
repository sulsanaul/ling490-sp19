from rule import Rule

class Grammar:

    def __init__(self, rules):
        self.rules = rules

    @staticmethod
    def readLines(grammarFile):
        rules = []
        for line in grammarFile:
            rules.append(Rule.readLine(line))
        return Grammar(rules)

    def findInitiallyNullableSymbols(self):
        unaryBranchingLhsSet = set()

        for rule in self.rules:
            if not rule:
                unaryBranchingLhsSet.add(rule.lhs)

        return unaryBranchingLhsSet

    def findMoreNullableSymbols(self, nullableSymbols):
        symbols = set()

        for rule in self.rules:
            if rule.lhs not in nullableSymbols:
                ifSymbolsInSet = True

                for obj in rule.rhs:
                    if obj not in nullableSymbols:
                        ifSymbolsInSet = False
                        break
                if ifSymbolsInSet:
                    symbols.add(rule.lhs)

        return symbols

    def findNullableSymbols(self):
        initSet      = self.findInitiallyNullableSymbols()
        secondarySet = self.findMoreNullableSymbols(initSet)
        while len(secondarySet) > 0:
            initSet.update(secondarySet)
            secondarySet = self.findMoreNullableSymbols(initSet)
        return initSet
