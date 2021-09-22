# Context-free grammars

## Symbol

* Create a file called symbol.py
* In that file define a class called Symbol
* The Symbol constructor should take a parameter called value. The constructor should initialize a single member variable called self.value.
  * If the provided value is None, the constructor should store None as the value of this Symbol
  * Otherwise, the constructor should store a string representation of value as the value of this Symbol
* The following builtin Python functions should work with Symbol:
  * ==
    * If the other item in the comparison is a Symbol, this should check to see if the values of the two Symbols are equal.
    * Otherwise this should return the value NotImplemented
  * hash()
    * This function should return the same value as running hash() on the Symbol's value
  * str()
    * If the Symbol's value is None, this should return the string representing the Greek small letter epsilon (Unicode codepoint U+03B5)
    * Otherwise, it should return self.value
  * bool()
    * This function should return False if the Symbol's value is None, and True otherwise
  * len()
    * If the Symbol's value is None, this should return 0
    * Otherwise, it should return the length of the Symbol's value
* In addition, the Symbol class should have the following member functions implemented:
  * isEpsilon()
    * This function should return False if the Symbol's value is None, and True otherwise
  * isNonterminal()
    * This function should return True if the first character of the Symbol's value is an uppercase letter, False otherwise
  * isTerminal()
    * This function should return False if the first character of the Symbol's value is an uppercase letter, True otherwise



## Rule

* Create a file called rule.py
* In that file define a class called Rule
* The Rule constructor should take parameters called lhs and rhs.
  * The lhs parameter should be a nonterminal Symbol object that corresponds to the left-hand side of a context-free rule.
    * If it is not, raise a Runtime error with an informative error message
    * Otherwise, store this parameter in a member variable called self.lhs
  * The rhs parameter should be a non-empty list of Symbol objects that corresponds to the right-hand side of a context-free rule.
    * If it is not, raise a Runtime error with an informative error message
    * Otherwise, store this parameter in a member variable called self.rhs
* The following builtin Python functions should work with Rule:
  * ==
    * If the other item in the comparison is also a Rule, this should check to see if the string representations of the two Rule objects are equal.
    * Otherwise this should return the value NotImplemented
  * hash()
    * This function should return the same value as running hash() on the Rule's string representation
  * str()
    * This function should return a string consisting of the string representation of the LHS symbol, followed by a space, followed by a rightward arrow (Unicode codepoint U+2192), followed by a space, followed by the string representation(s) of the RHS symbol(s), separated by spaces. For example:
       * "S → NP VP"
       * "DT → ε"
  * bool()
    * This function should return False if the number of RHS symbols is 1 and that RHS symbol isEpsilon, True otherwise
  * len()
    * This function should return the number of RHS symbols in self.rhs
* In addition, the Rule class should have the following @staticmethod function implemented:
  * readLine(line)
    * The line parameter should be treated as a space-delimited sequence of strings representing Symbols
    * If Rule.readline(line) is called and line is a string representing a nonterminal, it should return a corresponding unary-branching Rule with that nonterminal as the LHS symbol and a single epsilon RHS symbol
    * Otherwise, the first symbol in line should be treated as the LHS symbol and the rest should be treated as RHS symbols; a corresponding Rule should be returned


## Grammar

* Create a file called grammar.py
* In that file define a class called Grammar
* The Grammar constructor should take a parameter called rules
  * The rules parameter should be a list of Rule objects
  * The rules parameter should be stored in a member variable called self.rules
* The Grammar class should have a @staticmethod called readLines that takes a parameter called grammarFile
  * The grammarFile parameter should be a Python file object
  * the readLines() method should read each line from grammarFile
  * for each line in grammarFile, a new Rule should be created using Rule.readline()
  * the method should return a Grammar object that contains the list of rules from the file
* The Grammar class should have a method called findInitiallyNullableSymbols()
  * That method should return the set of symbols that appear on the left-hand side of unary-branching rules where the right-hand side is epsilon
* The Grammar class should have a method called findMoreNullableSymbols() that takes a parameter called nullableSymbols
  * That method should behave as follows: Given a set of nullable symbols, returns a new set of nullable symbols; The returned set will consist of symbols that appear on the left-hand side of rules in which all symbols on the right-hand side are in the initial set of nullable symbols
* The Grammar class should have a method called findNullableSymbols. This method should return all nullable symbols in the grammar

