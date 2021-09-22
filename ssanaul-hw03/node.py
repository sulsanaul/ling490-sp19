class Node:

    def __init__(self, max_size):
        """
		Constructs a new empty Node object.

        This constructor stores max_size in a member variable called self.max_size

        This constructor initializes a list called self.children
           with max_size elements, all of which are initially None

        This constructor initializes a member variable called self.num_children
           with an initial value of zero.

        This constructor initializes a member variable called self.value
           with an initial value of None
        """
        self.max_size = max_size
        self.children = [None]*max_size
        self.num_children = 0
        self.value = None


    def __contains__(self, index):
        """
		This method returns False if self.children[index] contains the value None,
        and returns True otherwise.
        """
        return False if self.children[index] is None else True


    def __len__(self):
        """
		Returns the number items stored in self.children that are not None
		"""
        return self.num_children

    def __getitem__(self, index):
        """
		Returns the existing item at self.children[index] that item is not None.

        Otherwise, stores a new Node at self.children[index], and returns that Node.
        This will cause self.num_children to increment by one.
        The newly created Node should have the same max_size as this Node.
		"""
        if self.children[index] is None:
            self.children[index] = Node(self.max_size)
            self.num_children += 1
        return self.children[index]

    def __setitem__(self, index, value):
        """
		Gets the Node stored at self[index], and sets the value of that Node to value
		"""
        n = self[index]
        n.value = value
