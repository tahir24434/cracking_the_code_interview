import bst

bbst = bst.BST()


def sorted_arr_to_balanced_bst_util(A, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = bst.BSTNode(A[mid])
    root.left = sorted_arr_to_balanced_bst_util(A, start, mid-1)
    root.right = sorted_arr_to_balanced_bst_util(A, mid+1, end)
    return root

