import unittest


class RBNode:
    def __init__(self, val, color=True) -> None:
        self.color = color
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def preorder(self, arr: list):
        if self.val is not None:
            arr.append(f"{self.val}: {self.color}")
        if self.left is not None:
            self.left.preorder(arr)
        if self.right is not None:
            self.right.preorder(arr)

    def inorder(self, arr: list):
        if self.left is not None:
            self.left.inorder(arr)
        if self.val is not None:
            arr.append(self.val)
        if self.right is not None:
            self.right.inorder(arr)


class RBTree:
    NIL = RBNode(None, False)

    def __init__(self) -> None:
        self.root: RBNode = self.NIL

    def _l_rotate(self, pivot: RBNode) -> None:
        # Get new root
        new_root = pivot.right
        # reassign childeren
        pivot.right = new_root.left

        # if child moving is not nil, change the parent
        if new_root.left != self.NIL:
            new_root.left.parent = pivot

        # reassign parent
        new_root.parent = pivot.parent

        # reassign root or child
        if pivot.parent is None:
            self.root = new_root
        elif pivot == pivot.parent.left:
            pivot.parent.left = new_root
        else:
            pivot.parent.right = new_root

        # add old root as new roots child
        new_root.left = pivot
        pivot.parent = new_root

    def _r_rotate(self, pivot) -> None:
        new_root = pivot.left
        pivot.left = new_root.right

        if new_root.right != self.NIL:
            new_root.right.parent = pivot

        new_root.parent = pivot.parent

        if pivot.parent is None:
            self.root = new_root
        elif pivot == pivot.parent.left:
            pivot.parent.left = new_root
        else:
            pivot.parent.right = new_root

        new_root.right = pivot
        pivot.parent = new_root

    def insert(self, val) -> None:
        # Make new node to add
        new_node = RBNode(val)
        new_node.left = new_node.right = self.NIL

        # Search for where to put it
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if current.val == val:
                return
            elif val < current.val:
                current = current.left
            else:
                current = current.right

        # Add the parent
        new_node.parent = parent

        # add as the correct child
        if parent is None:
            self.root = new_node
        elif val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Rebalance
        self._balance_insert(new_node)

    def _balance_insert(self, current):
        while current.parent is not None and current.parent.color:
            if current.parent == current.parent.parent.left:
                uncle = current.parent.parent.right
                if uncle.color:
                    current.parent.color = False
                    uncle.color = False
                    current.parent.parent.color = True
                    current = current.parent.parent
                else:
                    if current == current.parent.right:
                        current = current.parent
                        self._l_rotate(current)
                        parent = current.parent
                    parent.color = False
                    parent.parent.color = True
                    self._r_rotate(parent.parent)

            else:  # symmetric argument
                uncle = parent.parent.left
                if uncle.color:
                    parent.color = False
                    uncle.color = False
                    parent.parent.color = True
                    current = parent.parent
                else:
                    if current == parent.left:
                        current = parent
                        self._r_rotate(current)
                    current.parent.color = False
                    current.parent.parent.color = True
                    self._l_rotate(current.parent.parent)

        self.root.color = False

    def delete(self, val):
        pass

    def _balance_delete(self, current):
        pass

    def preorder(self) -> list:
        arr = []
        self.root.preorder(arr)
        return arr

    def inorder(self) -> list:
        arr = []
        self.root.inorder(arr)
        return arr
#


class TestRBTreeInsertion(unittest.TestCase):
    def setUp(self):
        self.tree = RBTree()

    def test_insert_root(self):
        # Insert root node, should be black
        self.tree.insert(10)
        self.assertEqual(self.tree.root.val, 10)
        self.assertFalse(self.tree.root.color)  # root is black

    def test_insert_red_child(self):
        # Insert root and one child, child should be red
        self.tree.insert(10)
        self.tree.insert(5)
        self.assertFalse(self.tree.root.color)
        self.assertTrue(self.tree.root.left.color)
        self.assertEqual(self.tree.root.left.val, 5)

    def test_insert_causes_recoloring(self):
        # Insert 3 nodes in such a way uncle is red, recoloring occurs
        self.tree.insert(10)  # Black root
        self.tree.insert(5)   # Red left child
        self.tree.insert(15)  # Red right child
        # Both children of root red -> recoloring should happen
        self.assertFalse(self.tree.root.color)
        self.assertFalse(not self.tree.root.left.color)
        self.assertFalse(not self.tree.root.right.color)

    def test_insert_causes_left_rotation(self):
        # Insert nodes to cause left rotation (right child is red, left child black)
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(20)  # Causes left rotation on 15
        # Root should remain black
        self.assertFalse(self.tree.root.color)
        # Check if 15's right child is 20 and 20 is red
        node_15 = self.tree.root.right
        self.assertEqual(node_15.val, 15)
        self.assertEqual(node_15.right.val, 20)
        self.assertTrue(node_15.right.color)

        # Insert nodes to cause right rotation (left child is red, right child black)
    def test_insert_causes_right_rotation(self):
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(10)  # Causes right rotation at 30
        self.assertEqual(self.tree.root.val, 20)
        self.assertFalse(self.tree.root.color)
        self.assertEqual(self.tree.root.left.val, 10)
        self.assertTrue(self.tree.root.left.color)
        self.assertEqual(self.tree.root.right.val, 30)
        self.assertTrue(self.tree.root.right.color)

    def test_insert_causes_left_right_rotation(self):
        # Insert nodes to cause left-right rotation pattern
        self.tree.insert(10)
        self.tree.insert(30)
        # Insert that should cause left rotation on 30, then right rotation on 10
        self.tree.insert(20)
        self.assertFalse(self.tree.root.color)
        self.assertEqual(self.tree.root.val, 20)
        self.assertTrue(self.tree.root.color is False)
        self.assertEqual(self.tree.root.left.val, 10)
        self.assertEqual(self.tree.root.right.val, 30)

    def test_insert_causes_right_left_rotation(self):
        # Insert nodes to cause right-left rotation pattern
        self.tree.insert(30)
        self.tree.insert(10)
        # Insert that should cause right rotation on 10, then left rotation on 30
        self.tree.insert(20)
        self.assertFalse(self.tree.root.color)
        self.assertEqual(self.tree.root.val, 20)
        self.assertEqual(self.tree.root.left.val, 10)
        self.assertEqual(self.tree.root.right.val, 30)


if __name__ == "__main__":
    unittest.main()


#
