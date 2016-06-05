import operator


def merge(left, right, compare):
    """
    Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.
    """
    result = []
    li = 0
    ri = 0

    while li < len(left) and ri < len(right):
        if compare(left[li], right[ri]):
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1

    # Copy leftovers (if any)
    while li < len(left):
        result.append(left[li])
        li += 1

    while ri < len(right):
        result.append(right[ri])
        ri += 1
    return result


def merge_sort(A, compare=operator.lt):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left = merge_sort(A[:mid], compare)
    right = merge_sort(A[mid:], compare)
    return merge(left, right, compare)

alist = [54,26,93,17,77,31,44,55,20]
result = merge_sort(alist)
print(result)