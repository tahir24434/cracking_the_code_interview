# left <= current < right


class BSTNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def bst_checker(root):
    node_and_bound_stack = [(root, -float('inf'), float('inf'))]
    while len(node_and_bound_stack):
        node, min, max = node_and_bound_stack.pop()
        if (node.key <= min) or (node.key > max):
            return False
        if node.left:
            node_and_bound_stack.append((node.left, min, node.key))
        if node.right:
            node_and_bound_stack.append((node.right, node.key, max))
    return True


# Instead of allocating a stack ourselves, we could write a recursive function that uses the call stack ↴ .
def bst_checker_rec(root, mini=-float('inf'), maxi=float('inf')):
    # An empty tree is BST
    if root is None:
        return True
    if (root.key <= mini) and (root.key > maxi):
        return False
    return bst_checker_rec(root.left, mini, root.key) and bst_checker_rec(root.right, root.key, maxi)
