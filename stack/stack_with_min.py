import stacks

class MinStack(object):
    def __init__(self):
        self.items = stacks.Stack()
        self.mins = stacks.Stack()

    def push(self, item):
        """
        adds a new item to the top of the stack. It needs the item and returns nothing.
        """
        self.items.push(item)
        if (self.mins.isEmpty()) or item <= self.mins.peek():
            self.mins.push(item)

    def pop(self):
        """
        removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
        """
        item = self.items.pop()
        if item == self.mins.peek():
            self.mins.pop()
        return item

    def min(self):
        return self.mins.peek()

    def peek(self):
        """
        returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
        """
        return self.items.peek()

    def isEmpty(self):
        """
        tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
        """
        return self.items.isEmpty()


s = MinStack()
print ("isEmpty=%s" % s.isEmpty())
s.push(2)
s.push(3)
print (s.min())
s.push(4)
s.push(1)
print (s.min())
s.pop()
print (s.min())
s.push(0)
print (s.min())
# pop from empty list will throw error.