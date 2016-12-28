
def binary_search(arr, elem_to_search, left, right):
    while right >= left:
        mid = (left + right) // 2
        if arr[mid] > elem_to_search:
            right = mid - 1
        elif arr[mid] < elem_to_search:
            left = mid + 1
        elif arr[mid] == elem_to_search:
            return mid
    return -1


if __name__ == "__main__":
    array = [1, 5, 7, 11, 13, 17]
    l = 0
    r = len(array) - 1
    print (binary_search(array, 5, l, r))
