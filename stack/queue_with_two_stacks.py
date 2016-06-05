import stacks


class Queue(object):
    def __init__(self):
        self.in_stack = stacks.Stack()
        self.out_stack = stacks.Stack()

    def push(self, item):
        self.in_stack.push(item)

    def pop(self):
        if self.out_stack.isEmpty():
            while not self.in_stack.isEmpty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()


q = Queue()
q.push(5)
q.push(6)
q.push(7)
print (q.pop())
q.push(8)
print (q.pop())
print (q.pop())
q.push(9)
q.push(10)
print (q.pop())
print (q.pop())
q.push(11)
print (q.pop())
q.push(12)
print (q.pop())
print (q.pop())