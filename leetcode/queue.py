class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, i):
        self.stack1.append(i)


    def dequeue(self):
        if not self.stack2:
            self.transfer()

        return self.stack2.pop()


    def peek(self):
        if not self.stack2:
            self.transfer()

        return self.stack2[-1] if self.stack2 else None


    def transfer(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
