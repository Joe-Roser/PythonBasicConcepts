# Important data structures

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

class BinaryTreeNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val == None:
            self.val = val
            return
        if self.val == val:
            return

        if val < self.val:
            if self.left == None:
                self.left = BinaryTreeNode(val)
                return
            self.left.insert(val)
        else:
            if self.right == None:
                self.right = BinaryTreeNode(val)
                return
            self.right.insert(val)

    def get_min(self):
        if self.left:
            return self.left.get_min()
        return self.val

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.val

    def delete(self, val):
        if self.val == None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val) 
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val) 
            return self
        #val == self.val
        if self.left == None:
            return self.right
        if self.right == None:
            return self.left
        
        node = self.right
        while node.left:
            node = node.left
        self.val = node.val
        self.right = self.right.delete(self.val)
        return self

    def contains(self, val):
        if self.val == None:
            return False
        if self.val == val:
            return True
        if val < self.val:
            if self.left:
                return self.left.contains(val)
            return False
        if self.right:
            return self.right.contains(val)
        return False

    def preorder(self, arr: list) -> list:
        if self.val == None:
            return arr
        arr.append(self.val)
        if self.left:
            arr = self.left.preorder(arr)
        if self.right:
            arr = self.right.preorder(arr)
        return arr

    def postorder(self, arr: list) -> list:
        if self.val == None:
            return arr
        if self.left:
            arr = self.left.postorder(arr)
        if self.right:
            arr = self.right.postorder(arr)
        arr.append(self.val)
        return arr

    def inorder(self, arr: list) -> list:
        if self.val == None:
            return arr
        if self.left:
            arr = self.left.inorder(arr)
        arr.append(self.val)
        if self.right:
            arr = self.right.inorder(arr)
        return arr

    def height(self) -> int:
        if self.val == None:
            return 0

        def check_height(node) -> int:
            if node:
                return node.height()
            return 0

        l_height = check_height(self.left)
        r_height = check_height(self.right)
        return max(l_height, r_height) + 1
#

class RBNode:
    def __init__(self, val, color=True) -> None:
        self.color = color
        self.parent = None
        self.left = None
        self.right = None
        self.val = val
        pass

class RBTree:
    def __init__(self) -> None:
        self.root = RBNode(None)

    def l_rotate(self, pivot: RBNode) -> None:
        pass

    def r_rotate(self, pivot) -> None:
        pass

    def insert(self, val) -> None:
        pass

    def ins_balance(self, pivot):
        pass

    def delete(self, val):
        pass

    def del_balance(self, pivot):
        pass
