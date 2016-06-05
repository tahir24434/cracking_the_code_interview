# There is an array of non-negative integers. A second array is formed by shuffling the elements of the first array
# and deleting a random element. Given these two arrays, find which element is missing in the second array.
# http://www.ardendertat.com/2011/09/27/programming-interview-questions-4-find-missing-element/#sthash.Wd4g6B9j.dpuf


# Using dictionary.
# O(n) with O(N) space.
def find_missing_dict(A, B):
    count_dict = dict()
    for item in B:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    for item in A:
        if item in count_dict:
            count_dict[item] -= 1
            if count_dict[item] < 0:
                return item
        else:
            return item


# Using XOR.
# if we XOR a number two times with some number nothing will change
# O(n) with no extra space.
def find_missing_xor(A, B):
    missing = 0
    for num in A + B:
        missing ^= num
    return missing

A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4]
missing_elem = find_missing_dict(A, B)
print (missing_elem)
missing_elem = find_missing_xor(A, B)
print (missing_elem)

A = [1, 2, 3, 3]
B = [1, 2, 3]
missing = find_missing_dict(A, B)
print (missing)
missing = find_missing_xor(A, B)
print (missing)

