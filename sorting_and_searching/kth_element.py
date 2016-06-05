def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


# Return rank of element A[r] in array A.
def partition(A, p, r):
    pivot = A[r]
    small = p - 1
    for j in range(p, r):
        if A[j] < pivot:
            small += 1
            swap(A, j, small)

    swap(A, small+1, r)
    # print ("%d rank element is %d" % (small+1, pivot))
    print (A)
    return small + 1 # Rank


def find_rank(A, p, r, k):
    while p <= r:
        rank = partition(A, p, r)
        if k > rank:
            p = rank + 1
        elif k < rank:
            r = rank - 1
        elif k == rank:
            return A[rank]


k = int(input("enter desired rank: "))
# A = [0, 1, 2, 3, 4, 7, 9, 11, 23, 70, 90]
A = [4, 3, 1, 7, 9, 11, 0, 2, 90, 70, 23]
element = find_rank(A, 0, len(A) - 1, k)
print ("%d rank element is %d" %(k, element))


# median of medians can be used as well.