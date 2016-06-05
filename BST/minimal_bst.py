import bst
# Given a sorted array with unique integer elements, write an algorithm to create a BST with minimal height.


def create_minimal_bst(A, start, end):
    if end < start:
        return
    mid = (start + end) // 2
    root = bst.BSTNode(A[mid])
    root.left = create_minimal_bst(A, start, mid)
    root.right = create_minimal_bst(A, mid, end)
    return root