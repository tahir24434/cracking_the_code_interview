# You are given an array-like data structure Listy which lacks a size method. It does, however, have an elementAt(i)
# method that returns the element at index i in O(1) time. If i is beyond the bounds of the data structure, it
# returns -1 (For this reason, the data structure only supports positive integers). Given a Listy which contains
# sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return
# any index.


def elementAt(A, i):
    try:
        element = A[i]
    except IndexError:
        element = -1

    return element


def right_index(A, item):
    idx = 1
    while (elementAt(A, idx) >= 0) and (elementAt(A, idx) <= item):
        idx *= 2
    return idx


def search(A, item):
    li = 0
    ri = right_index(A, item)

    while li <= ri:
        mid = (li + ri) // 2
        print ("li:%d, ri:%d, mid:%d" % (li, ri, mid))
        if elementAt(A, mid) == -1:
            ri = mid - 1
        elif A[mid] > item:
            ri = mid - 1
        elif A[mid] < item:
            li = mid + 1
        elif A[mid] == item:
            return mid
        input("press enter")

A = [3, 4, 5, 6, 7, 8, 9]
idx = search(A, 90)
print (idx)
