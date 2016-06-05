def insertion_sort(A):
    for i in range(1, len(A)):
        item_to_insert = A[i]
        current_index = i

        while current_index > 0 and A[current_index-1] > item_to_insert:
            A[current_index] = A[current_index-1]
            current_index -= 1
        A[current_index] = item_to_insert

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)