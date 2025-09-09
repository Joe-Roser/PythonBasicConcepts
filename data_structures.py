# Important data structures

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None

        return self.items.pop

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() == 0:
            return None

        return self.items[-1]

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.push(item)

    def pop(self):
        if self.size() == 0:
            return None

        return self.items.pop

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() == 0:
            return None

        return self.items[-1]
    

