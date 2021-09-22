# Context-free grammars

## Previous files

* Copy your symbol.py file from the previous HW
* Copy your rule.py file from the previous HW
* Copy your grammar.py file from the previous HW

## Extend Grammar class

* Add a method called removeEpsilons(self) to the Grammar class.
  * That method should return a new Grammar object that is equivalent to self but which contains no epsilons
* Add a method called removeUnaryRules(self) to the Grammar class.
  * That method should return a new Grammar object that is equivalent to self but which contains no unary-branching rules in which the right-hand side is a non-terminal
* Add a method called shortenLongRules(self) to the Grammar class.
  * That method should return a new Grammar object that is equivalent to self but in which the right-hand side of every rule contains no more than two symbols
* Add a method called makeTerminalsUnary(self) to the Grammar class.
  * That method should return a new Grammar object that is equivalent to self but in which every terminal is found only as the right-hand side of a unary-branching rule
