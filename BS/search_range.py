# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# Example:
# Given [5, 7, 7, 8, 8, 10]
# and target value 8,
# return [3, 4].

def searchRange(A, B):
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right) // 2
            if A[mid] == B:
                break
            elif A[mid] < B:
                left = mid + 1
            else:
                right = mid - 1

        left = mid
        right = mid

        while A[left] == B and left > 0 and A[left-1] == B:
            left -= 1
        while A[right] == B and right < len(A)-1 and A[right + 1] == B:
            right += 1
        return [left, right]

A = [1, 3, 5, 8, 8, 9]
B = 8
print (searchRange(A, B))

A = [1]
B = 1
print (searchRange(A, B))
