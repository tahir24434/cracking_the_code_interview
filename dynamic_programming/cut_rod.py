# Given a rod of length n inches and a table of prices pi for i = 1, 2, ..., n, determine the maximum revenue
# rn obtainable by cutting up the rod and selling the prices.
import time

def cut_rod(p, n):
    if n == 0:
        return 0
    else:
        rev = -1
        for i in range(1, n+1):
            rev = max(rev, p[i] + cut_rod(p, n-i))
        return rev

memo_dict = {}
def cut_rod_memoized(p, n):
    if n == 0:
        return 0
    elif n in memo_dict:
        return memo_dict[n]
    else:
        rev = -1
        for i in range(1, n+1):
            rev = max(rev, p[i] + cut_rod_memoized(p, n-i))
    memo_dict[n] = rev
    return rev
memo_dict.clear()


def cut_rod_bottom_up(p, n):
    memo_dict[0] = 0
    for j in range(1, n+1):
        rev = -1
        for i in range(1, j + 1):
            rev = max(rev, p[i] + memo_dict[j-i])
        memo_dict[j] = rev
    return memo_dict[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 31, 33, 33, 35, 36, 40, 42, 43, 44, 44, 45, 46, 47, 48, 49, 50, 51]

time1 = time.time()
print (cut_rod(p, 21))
time2 = time.time()
print ('naive function took %0.3f ms' % ((time2-time1)*1000.0))

time1 = time.time()
print (cut_rod_memoized(p, 21))
time2 = time.time()
print ('memoized function took %0.3f ms' % ((time2-time1)*1000.0))

time1 = time.time()
print (cut_rod_bottom_up(p, 21))
time2 = time.time()
print ('memoized function took %0.3f ms' % ((time2-time1)*1000.0))