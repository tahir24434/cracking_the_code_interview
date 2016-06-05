# Property:
#   for any node x:
#   - For all nodes y in the left subtree of x:
#     key[y] <= key[x]
#   - For all nodes y in the right subtree of x:
#     key[y] >= key[x]

class BSTNode(object):
    def __init__(self, t):
        """
        Each node of the tree holds the following information:
            - x.key    - Value stored in node x
            - x.left   - Pointer to the left child of node x. NIL if x has no left child
            - x.right  - Pointer to the right child of node x. NIL if x has no right child
            - x.parent - Pointer to the parent node of node x. NIL if x has no parent, i.e. x is the root of the tree
        """
        self.key = t
        self.left = None
        self.right = None
        self.parent = None

    def hasRightChild(self):
        return self.right

    def hasLeftChild(self):
        return self.left

    def rightChild(self):
        return self.right

    def leftChild(self):
        return self.left

class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key):
        # if tree is empty
        new = BSTNode(key)
        if self.root is None:
            self.root = new
        else:
            self.insert(new)
        self.size += 1
        return new

    def insert(self, node):
        """
        The procedure takes a node 'node' for which
        node.key=key,  node.left=NIL and node.right=NIL.
        It modifies T and some of the attributes of 'node' in such a way that it inserts 'node' into an appropriate
        position in the tree.
        """
        current_root = self.root
        key = node.key
        while True:
            if key < current_root.key:
                # Go left.
                # But before that check, if left contains something. If there is nothing then, place new there.
                if current_root.left is None:
                    current_root.left = node
                    node.parent = current_root
                    break
                current_root = current_root.left
            else:
                # Go right.
                # But before that check, if right contains something. If there is nothing then, place new there.
                if current_root.right is None:
                    current_root.right = node
                    node.parent = current_root
                    break
                current_root = current_root.right

    def remove(self, key):
        # If tree is empty, then there is nothing to be deleted.
        if self.size == 0:
            raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key: # One has to change BST properties
            self.root = None
            self.size -= 1
        else:
            # Find key in tree
            node_to_delete = self.find(key)
            if node_to_delete:
                self.delete(node_to_delete)
            else:
                raise KeyError('Error, key not in tree')

    def delete(self, node):
        print ("TODO: delete")

    def find(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = self.root
        while node is not None:
            if t == node.key:
                return node
            elif t < node.key:
                # Go left
                node = node.left
            else:
                # Go right
                node = node.right
        return None

    # We can always find an element in binary search tree whose key is minimum by following the left child pointers
    # from the root until we encounter a Nil.
    # The following procedure returns a pointer to the minimum element in the subtree rooted at given node "node".
    def treeMinimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # We can always find an element in binary search tree whose key is maximum by following the right child pointers
    # from the root until we encounter a Nil.
    # The following procedure returns a pointer to the maximum element in the subtree rooted at given node "node".
    def treeMaximum(self, node):
        # We can always find an element in binary search tree whose key is maximum by following the right child pointers
        # from the root untill we encounter a Nil.
        current = node
        while current.right is not None:
            current = current.right
        return current

    # If all the keys are distinct then successor of a node "node" is the node with the smallest key greater than x.key.
    # In other words, it is next highest element in sorted order.
    # The following procedure returns the successor of a node with x in a binary search tree if it exists and Nil if
    # x has the largest key in the tree.
    def tree_successor(self, node):
        # If x has the right child (right subtree), find smallest element in right subtree.
        if node.hasRightChild():
            return self.treeMinimum(node.right)
        # if no right subtree, keep moving up as long as x remains right child of ancestor. The moment when x
        # becomes left child of its ancestor, you find your desired successor.
        ancestor = node.parent
        while ancestor is not None and node == ancestor.right: # While n is right child of parent.
            node = ancestor # Move up.
            ancestor = ancestor.parent
        return ancestor

    # If all the keys are distinct then predecessor of node 'node' is the node with the largest key smaller than x.key.
    # In other words, it is previous largest element in sorted order.
    # The following procedure returns the predecessor of a node with x in a binary search tree if it exists and Nil if
    # x has the smallest key in the tree.
    def tree_predecessor(self, node):
        # If x has the right child (right subtree), find smallest element in right subtree.
        if node.hasLeftChild():
            return self.treeMaximum(node.left)
        # if no left subtree, keep moving up as long as x remains left child of ancestor. The moment when x
        # becomes right child of its ancestor, you find your desired predecessor.
        ancestor = node.parent
        while ancestor is not None and node == ancestor.left: # While n is right child of parent.
            node = ancestor # Move up.
            ancestor = ancestor.parent
        return ancestor

    def second_largest(self, node):
        maximum = self.treeMaximum(node)
        if maximum.left is None:
            second_largest = maximum.parent
        else:
            second_largest = self.treeMinimum(maximum.left)
        return second_largest.key


    @staticmethod
    def in_order_tree_walk(root):
        """
        Print tree content inorder
        """
        if root is not None:
            BST.in_order_tree_walk(root.left)
            print (root.key)
            BST.in_order_tree_walk(root.right)

    @staticmethod
    def pre_order_tree_walk(root):
        """
        Print tree content preorder
        """
        if root is not None:
            print (root.key)
            BST.pre_order_tree_walk(root.left)
            BST.pre_order_tree_walk(root.right)

    @staticmethod
    def post_order_tree_walk(root):
        """
        Print tree content post-order
        """
        if root is not None:
            BST.post_order_tree_walk(root.left)
            BST.post_order_tree_walk(root.right)
            print (root.key)

    @staticmethod
    def nth_largest_element_util(root, n, c):
        if root is None or c[0] > n:
            return
        BST.nth_largest_element_util(root.right, n, c)
        c[0] += 1
        if c[0] == n:
            print ("%dth largest element is %d" % (n, root.key))
        BST.nth_largest_element_util(root.left, n, c)

    @staticmethod
    def nth_largest_element(root, n):
        """
        Print tree content in-order
        """
        c = [0]
        BST.nth_largest_element_util(root, n, c)

    @staticmethod
    def nth_smallest_element_util(root, n, c):
        if root is None or c[0] > n:
            return
        BST.nth_smallest_element_util(root.left, n, c)
        c[0] += 1
        if c[0] == n:
            print ("%dth smallest element is %d" % (n, root.key))
        BST.nth_smallest_element_util(root.right, n, c)

    @staticmethod
    def nth_smallest_element(root, n):
        """
        Print tree content in-order
        """
        c = [0]
        BST.nth_smallest_element_util(root, n, c)

    @staticmethod
    def node_count(root):
        if root is None:
            return 0
        return BST.node_count(root.left) + BST.node_count(root.right) + 1

    @staticmethod
    def leaves_count(root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        return BST.leaves_count(root.left) + BST.leaves_count(root.right)


def test(args=None, BSTtype=BST):
    tree = BSTtype()
    tree.put(29)
    tree.put(26)
    print ("root:%s, left:%s, right:%s" %(tree.root.key, tree.root.left.key, tree.root.right))
    print ("root_height:%s, left_height:%s" % (tree.root.height, tree.root.left.height))
    tree.put(23)
    try:
        print ("root:%s, left:%s, right:%s" %(tree.root.key, tree.root.left.key, tree.root.right.key))
    except:
        print ("root:%s, left:%s, right:None" %(tree.root.key, tree.root.left.key))
    print ("root_height:%s, left_height:%s" % (tree.root.height, tree.root.left.height))
    minimum = tree.treeMinimum(tree.root)
    maximum = tree.treeMaximum(tree.root)
    print ("minimum:%s. maximum::%s" % (minimum.key, maximum.key))
    print (tree.root.key)
    tree.put(50)
    tree.put(51)
    tree.put(52)
    tree.put(53)
    print ("root_height:%s, left_height:%s" % (tree.root.height, tree.root.left.height))
    print (tree.root.key)


def test1(args=None, BSTtype=BST):
    tree = BSTtype()
    i = 0
    while (1):
        response = int(input("Please enter number: "))
        tree.put(response)
        BST.post_order_tree_walk(tree.root)
        minimum = tree.treeMinimum(tree.root)
        maximum = tree.treeMaximum(tree.root)
        count = BST.node_count(tree.root)
        if i >= 1:
            sec_largest = tree.second_largest(tree.root)
            print ("sec_largest:%s" % sec_largest)
        print ("minimum:%s. maximum::%s, count:%s" % (minimum.key, maximum.key, count))
        successor = tree.tree_successor(tree.root)
        if successor:
            print ("successor:%s" % successor.key)
        i += 1

if __name__ == '__main__': test1()