# Given a sorted array and a number x, find a pair in array whose sum is closest to x.

def pair_with_closest_sum(A, target_sum):
    left, right = 0, len(A)-1
    diff = float("infinity")

    while left < right:
        pair_sum = A[left] + A[right]

        if (abs(pair_sum - target_sum) < diff):
            diff = abs(pair_sum - target_sum)
            pair = (A[left], A[right])

        if pair_sum < target_sum:
            left += 1
        elif pair_sum > target_sum:
            right -= 1
        elif pair_sum == target_sum:
            return (A[left], A[right])

    return pair

A = [10, 22, 28, 29, 30, 40]
print (pair_with_closest_sum(A, 54))