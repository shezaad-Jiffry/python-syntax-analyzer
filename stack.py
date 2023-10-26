class Stack:
    '''
    class is made using the self.items feature in python to make a quick and efficent stack
    the approach with the stack is to pop from it everytime we need to check if a statement is valid so by line usually
    '''
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove the item from the top of the stack and return it."""

        return self.items.pop()

    def peek(self):
        """Return the top item from the stack without removing it."""
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    def clear(self):
        """Empties the stack"""
        self.items.clear()