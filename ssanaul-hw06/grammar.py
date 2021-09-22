    
from rule import Rule
from symbol import Symbol

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
    
    def removeEpsilons(self):
        nullableSymbols = self.findNullableSymbols()
        newRules = []
        for rule in self.rules:
            if rule:
                indices = [i for i, s in enumerate(rule.rhs) if s in nullableSymbols]
                for i in ps(indices):
                    rhs2 = rule.rhs.copy()
                    indices2 = reversed(sorted(i))
                    for j in indices2:
                        del rhs2[j]
                    if len(rhs2) > 0:
                        newRules.append(Rule(rule.lhs, rhs2))
        return Grammar(newRules)
                    
    
    def removeUnaryRules(self):
        newRules = []
        lhsSymbols = []
        rhsSymbols = []
        for rule in self.rules:
            if len(rule.rhs) == 1 and rule.rhs[0].isNonTerminal():
                rhsSymbols.append(rule.rhs[0])
                lhsSymbols.append(rule.lhs)
            else:
                newRules.append(rule)
        for rule in self.rules:
            if rule.lhs in lhsSymbols and len(rule.rhs) == 1 and rule.rhs[0].isTerminal():
                newRules.append(Rule(rhsSymbols[lhsSymbols.index(rule.lhs)], rule.rhs))
        return Grammar(newRules)
                
    
    def shortenLongRules(self):
        newRules = []
        n = 0
        for rule in self.rules:
            lhs = rule.lhs
            rhs = rule.rhs
            while len(rhs) > 2:
                n += 1
                s = Symbol('X'+str(n))
                newRules.append(Rule(lhs, [rhs[0], s]))
                lhs = s
                rhs = rhs[1:]
            newRules.append(Rule(lhs, rhs))
        return Grammar(newRules) 
             
    
    def makeTerminalsUnary(self):
        newRules = []
        rhs_dict = dict()
        n = 0
        for rule in self.rules:
            for symbol in rule.rhs:
                if symbol not in rhs_dict:
                    if symbol.isTerminal():
                        n += 1
                        s = Symbol('T'+str(n))
                        rhs_dict[symbol] = s
                        newRules.append(Rule(s, [symbol]))
                    else:
	                    rhs_dict[symbol] = symbol
            rhs = [rhs_dict[s] for s in rule.rhs]
            newRules.append(Rule(rule.lhs, rhs))
        return Grammar(newRules) 
	
def ps(set):
	if len(set) > 0:
		for subset in ps(set[1:]):
			yield subset
			yield subset[0:1] + subset
	else:
		yield []
