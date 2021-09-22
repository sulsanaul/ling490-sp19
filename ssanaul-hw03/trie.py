from node import Node

class Trie:

    def __init__(self):
        """
		Constructs a new Node called self.root with max_size=0x10FFFF+1
		"""
        self.root = Node(0x10FFFF+1)


    def store(self, sequence, startNode):
        """
		Stores the sequence in the trie, starting at startNode.

        This method creates new intermediate nodes if needed.
		"""
        for n in sequence:
            i = ord(n)
            startNode = startNode[i]
        return startNode
	

    def lookup(self, sequence, startNode):
        """
		If sequence is stored in the trie (starting at startNode), return the final node.
        Otherwise return None.
		"""
        for n in sequence:
            i = ord(n)
            if i in startNode:
                startNode = startNode[i] 
            else:
                return None
        return startNode
		

    def __contains__(self, sequence):
        """Returns True if sequence is stored in the trie, False otherwise"""
        return self.lookup(sequence, self.root)


    def __getitem__(self, sequence):
        """If sequence is stored in the trie, returns the value stored at the final node.
        Otherwise, raises a KeyError."""
        n = self.lookup(sequence, self.root)
        if n:
            return n.value
        else:
            raise KeyError


    def __setitem__(self, sequence, value):
        """Stores value as the value of the final node corresponding to the sequence"""
        n = self.store(sequence, self.root)
        n.value = value
