import sys


def counting_sort(A, p):
    count = [0] * 10    # 10 represents base here.
    output = [0] * len(A)
    # Count the number of occurances of any item.
    for item in A:
        count[int(item/p)%10] += 1

    # Count the number of elements which are less than equal to i.
    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(A)-1, -1, -1):
        output[count[int(A[i]/p)%10] - 1] = A[i]
        count[int(A[i]/p) % 10] -= 1

    return output


def radix_sort(A):
    # Find maximum element of array
    maxval = -sys.maxsize # Storing minimum possible value
    for item in A:
        maxval = max(maxval, item)

    p = 1
    pas = 1
    while int(maxval/p) > 0:
        A = counting_sort(A, p)
        print ("After pass "+ str(pas)+ " : "+str(A))
        p *= 10
        pas += 1

arr = [9892, 49282, 12228, 903, 9011, 292829, 5291]
print ("Initial Array: "+str(arr))
radix_sort(arr)
