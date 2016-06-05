import sys

# suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance,
# 1 2 3 4 5 might become 3 4 5 1 2.
# Devise a way to find an element in the rotated array in O(log n) time.

# If you divide the array at mid, one half of it will always be sorted. We have to look for sorted side, and see
# whether item lies on sorted side by checking corner items.

# Case1: A[mid] = item
# Case2: if A[mid] < A[right] (right side is sorted)
#           if item > A[mid] and item <= A[right]:
#               # Search on sorted side
#           else:
#               # Search on unsorted side.
# Case3: if A[left] < A[mid] (left side is sorted)
#           if item >= A[left] and item < A[mid]:
#               # Search on sorted side
#           else:
#               # Search on unsorted side.
# NOTE: Elements have to be distinct https://www.youtube.com/watch?v=uufaK2uLnSI (see last few mins).


def search_in_sorted_rotated_array(A, left, right, item):
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == item:
            return mid
        elif A[mid] < A[right]: # Right side is sorted
            if item > A[mid] and item <= A[right]:
                left = mid + 1 # Item is on right sorted side.
            else:
                right = mid -1
        elif A[mid] > A[left]: # Left side is sorted
            if item >= A[left] and item < A[mid]:
                right = mid - 1 # Item is on left sorted side
            else:
                left = mid+1

A = [5, 6, 8, 21, 22, 24, 1, 2, 3]
index = search_in_sorted_rotated_array(A, 0, len(A) - 1, 1)
print ("index = %s" % index)
A = [4, 5, 6, 0, 1, 2, 3]
index = search_in_sorted_rotated_array(A, 0, len(A) - 1, 0)
print ("index = %s" % index)