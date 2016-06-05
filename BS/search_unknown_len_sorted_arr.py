# Given a sorted array of unknown length and a number to search for, return the index of the number in the array.
# Accessing an element out of bounds throws exception. If the number occurs multiple times, return the index of any
# occurrence. If it is not present, return -1.

# Simple binary search will not work as we don't know the size of the array, hence upper-bound.
# We need to narrow down our search area.
# We can check indices 0, 2^0, 2^1, 2^2, ..., 2^n until we find element greater than equal to desired element or we
# hit out-of-bound exception.


def get_index(A, item):
    i = index = 0
    while True:
        try:
            if A[index] == elem_to_search:
                return index
            elif A[index] < elem_to_search:
                index = 2 ^ i
            else:
                # Binary search
                item_index = binary_search(index//2 + 1, index - 1, item)
                break
            i += 1
        except IndexError:
            break

    return item_index


def binary_search(left_index, right_index, item):
    while left_index <= right_index:
        mid = (left_index + right_index) // 2 # right: 8, left:2, 5
        if item > A[mid]:
            left_index = mid + 1
        elif item < A[mid]:
            right_index = mid - 1
        elif item == A[mid]:
            return mid
    return -1


A = [int(x) for x in input().split()]
elem_to_search = int(input())
print (get_index(A, elem_to_search))