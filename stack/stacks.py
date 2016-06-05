class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        adds a new item to the top of the stack. It needs the item and returns nothing.
        """
        self.items.append(item)

    def pop(self):
        """
        removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
        """
        return self.items.pop()

    def peek(self):
        """
        returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
        """
        return self.items[len(self.items)-1]

    def isEmpty(self):
        """
        tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
        """
        return self.items == []

    def size(self):
        """
        returns the number of items on the stack. It needs no parameters and returns an integer.
        """
        return len(self.items)

    def sort(self):
        sorted_st = Stack()
        while not self.isEmpty():
            tmp = self.pop()
            while (not sorted_st.isEmpty()) and tmp < sorted_st.peek():
                self.push(sorted_st.pop())
            sorted_st.push(tmp)
        self.items = sorted_st.items
