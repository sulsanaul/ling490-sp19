import sys

from grammar import *

class Cell:

    def __init__(self, value, left_child, right_child=None):
        """Initializes a CKY parse chart cell, storing a value 
		(that corresponds to the left-hand side of a context-free rule,
		a left-child (that corresponds to the first symbol on the 
		right-hand side of the context-free rule), and a right-child 
		(that is None if the rule is unary, or if the rule is binary 
		corresponds to the second symbol on the right-hand side of the context-free rule)."""
        self.value = value
        self.left_child = left_child
        if right_child:
            self.right_child = right_child[1]
        else:
            self.right_child = None
			
    def __str__(self):
        if self.right_child==None:
            return "(" + str(self.value) + " " + str(self.left_child) + ")"
        else:
            return "(" + str(self.value) + " " + str(self.left_child) + " " + str(self.right_child) + ")"

    def __repr__(self):
        if self.right_child==None:
            return "Cell(" + str(self.value) + ", " + str(self.left_child) + ")"
        else:
            return "Cell(" + str(self.value) + ", " + str(self.left_child) + ", " + str(self.right_child) + ")"


# The use of this function is optional, but strongly recommended
#
def num_cells(length):
    """Given length (the number of words in the sentence), returns the number of cells in the corresponding parse chart"""
    num_cells = 0
    for i in range(1, length):
	    num_cells += i 
    return num_cells

# The use of this function is optional, but strongly recommended
#
def cell_index(start, end, length):
    """Given length (the number of words in the sentence), as well as a span defined by a start and end index, returns an integer in the range [0, length). A call to this function with cell_index(0, length, length) should return zero."""
    pass


# The use of this class is optional, but strongly recommended
#
class Chart:

    def __init__(self, n):
        """Initializes a CKY parse chart for a sentence of length n"""
        self.cells = []
        for i in range(n, 0, -1):
            self.cells.append([None]*i)

    def get(self, start, end):
        """Returns a (possibly empty) list of Cell objects that span from start to end"""
        l = []
        for i in range(len(self.chart)):
            for j in range(len(chart[i])):
                l.append(chart[i][j])
        return l[start:end]

    def put(self, start, end, cell):
        """Stores a Cell object that spans from start to end"""
        pass

class Parser:

    def __init__(self, grammar):
        """Initializes a parser using the provided grammar"""
        self.grammar = grammar

    def parse(self, sentence):
        """Parses the provided sentence using the CKY algorithm"""
        chart = Chart(len(words)).cells
        lhs = []
        for i in range(len(words)):
            s = Symbol(words[i])
            for rule in self.grammar.rules:
                if s in rule.rhs:
                    lhs.append(rule.lhs)
                    chart[0][i] = Cell(rule.lhs, rule.rhs[0])
        for i in range(1, len(words)):
            for j in range(len(chart[i])):
                s = Symbol(str(chart[i-1][j].value)+str(chart[i-1][j+1].value))
                for rule in self.grammar.rules:
                    if s in rule.rhs:
                        chart[i][j] = Cell(rule.lhs, rule.rhs[0])
        return chart

if __name__ == "__main__":

    if len(sys.argv) < 2:

        print("Please provide a file as argument")

    else:

        fileName = sys.argv[1]
        #sentence

        with open(fileName) as grammar_file:

            grammar0 = Grammar.readLines(grammar_file)
            grammar1 = grammar0.removeEpsilons()
            grammar2 = grammar1.removeUnaryRules()
            grammar3 = grammar2.shortenLongRules()
            grammar4 = grammar3.makeTerminalsUnary()
            
            parser = Parser(grammar4)
            
            for line in sys.stdin:
                words = line.strip().split()
                result = parser.parse(words)
                print(result)
