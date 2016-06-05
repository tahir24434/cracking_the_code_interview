# Counting sort assumes that each of the n input elements is an integer in the range 0 to k.
def counting_sort(A):
    max_element = max(A)
    count = [0] * (max_element + 1)
    output = [0] * len(A)

    # Count number of individual elements
    # C[i] will contain the number of elements equal to i
    for item in A:
        count[item] += 1

    # Count number of elements less than equal to i
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # A: 4, 1, 3, 1, 0
    # count: 1, 2, 0, 1, 1
    # count: 1, 3, 3, 4, 5. We have 1 element which is less than equal to 0, 3 elements which are less than equal to 1.
    for i in range(len(A)):
        # There are count[element] items which are less than equal to element. So, element should go at index
        # "count[element-1]".
        # So, in-short, count is becoming index of output array for element.
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1

    print (output)

if __name__ == '__main__':
    # A = array to sort
    # B = array to hold sorted output
    # K = max element of array
    arr = [9892, 49282, 12228, 903, 9011, 292829, 5291]
    print ("Initial Array: " + str(arr))
    counting_sort(arr)
