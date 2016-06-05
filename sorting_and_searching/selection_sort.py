# The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order
# to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass,
# places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct
# place. After the second pass, the next largest is in place. This process continues and requires n-1 passes to
# sort n items, since the final item must be in place after the (n-1)st pass.

def swap_element(A, index1, index2):
    tmp = A[index1]
    A[index1] = A[index2]
    A[index2] = tmp


def selection_sort(A):
    num_passes = len(A) - 1
    while num_passes > 0:
        largest_elem_index = 0
        for i in range(1, num_passes+1):
            if A[i] > A[largest_elem_index]:
                largest_elem_index = i
        swap_element(A, largest_elem_index, num_passes)
        num_passes -= 1


alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)