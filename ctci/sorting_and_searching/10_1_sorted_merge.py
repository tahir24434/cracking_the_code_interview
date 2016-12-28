# You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.


# This solution assumes that array A fits array B perfectly(it becomes a full array).
# Time: O(a)
# Space: O(a)
def sorted_merge(A, B):
    A_idx = len(A) - len(B) - 1
    B_idx = len(B) - 1
    merged_idx = len(A) - 1

    while B_idx >= 0:
        if A[A_idx] > B[B_idx] and A_idx >= 0:
            A[merged_idx] = A[A_idx]
            A_idx -= 1
        else:
            A[merged_idx] = B[B_idx]
            B_idx -= 1

        merged_idx -= 1

if __name__ == "__main__":
    A = [1, 5, 7, 11, 12, None, None, None, None, None, None]
    B = [1, 3, 6, 8, 13, 14]
    sorted_merge(A, B)
    print (A)
