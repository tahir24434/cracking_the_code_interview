import binary_search

def search_in_sorted_array(arr, elem_to_search):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[left] < arr[mid]:
            return binary_search.binary_search(arr, elem_to_search, left, mid - 1)
        elif arr[right] > arr[mid]:
            return binary_search.binary_search(arr, elem_to_search, mid + 1, right)
        elif

if __name__ == "__main__":
    A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    elem_to_search = 5
