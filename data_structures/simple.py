class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)
#

class BadQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)
#

class BasicNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node
#

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node != None:
            yield node.val
            node = node.next

    def push(self, item):
        if self.tail == None:
            self.head = BasicNode(item)
            self.tail = self.head
            return
        self.tail.next = BasicNode(item)
        self.tail = self.tail.next

    def push_to_head(self, item):
        new_head = BasicNode(item)
        new_head.next = self.head
        if self.head == None:
            self.tail = new_head
        self.head = new_head

    def pop(self):
        if self.head == None:
            return None
        ret = self.head
        self.head = self.head.next
        return ret

    def peek(self):
        return self.head
#

