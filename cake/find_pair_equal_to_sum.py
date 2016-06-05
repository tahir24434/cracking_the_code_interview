# Find a pair of elements from an array whose sum equals a given number.


def find_pair(A, n):
    seen_elements = {}
    for element in A:
        compliment_element = n - element  # If n=10 and element=4, then compliment element is 6
        if compliment_element in seen_elements:
            return (element, compliment_element)
        else:
            seen_elements[element] = element

    return None


# Set has O(1) lookup complexity.
def find_pair_using_set(A, n) :
    seen_elements = set()
    for element in A:
        compliment_element = n - element  # If n=10 and element=4, then compliment element is 6
        if compliment_element in seen_elements:
            return (element, compliment_element)
        else:
            seen_elements.add(element)
    return None


# Above methods take O(n) time but also takes extra memory.
# Following method takes O(nlogn + n) time.
def find_pair_without_extra_memory(A, n):
    A.sort()
    i, j = 0, len(A) - 1
    while i < j:
        pair_sum =  A[i] + A[j]
        if pair_sum == n:
            return (A[j], A[i])
        elif pair_sum < n:
            i += 1
        else:
            j -= 1
    return None

A = [4, 3, 2, 1, 8, 7]
print (find_pair(A, 5))
print (find_pair(A, 6))
print (find_pair(A, 8))

print ("using set function")
print (find_pair_using_set(A, 5))
print (find_pair_using_set(A, 6))
print (find_pair_using_set(A, 8))

# [1, 2, 3, 4, 7, 8]
print ("using find_pair_without_extra_memory")
print (find_pair_without_extra_memory(A, 5))
print (find_pair_without_extra_memory(A, 6))
print (find_pair_without_extra_memory(A, 8))