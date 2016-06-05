import time

# Follow recursive definition
def fib_naive(n):
    if n <= 2:
        return 1
    fib = fib_naive(n-1) + fib_naive(n-2)
    return fib


# Remember the solution
memo_dict = {}
def fib_memoized(n):
    if n in memo_dict:
        return memo_dict[n]
    if n <= 2:
        return 1
    fib = fib_memoized(n-1) + fib_memoized(n-2)
    memo_dict[n] = fib
    return fib
memo_dict.clear()


def bottom_up_fib(n):
    for i in range(1, n):
        if i <= 2:
            fib = 1
        else:
            fib = memo_dict[i-2] + memo_dict[i-1]
        memo_dict[i] = fib
    return memo_dict[n]

time1 = time.time()
print (fib_naive(23))
time2 = time.time()
print ('naive function took %0.3f ms' % ((time2-time1)*1000.0))

time1 = time.time()
print (fib_memoized(23))
time2 = time.time()
print ('memoized function took %0.3f ms' % ((time2-time1)*1000.0))

time1 = time.time()
print (bottom_up_fib(23))
time2 = time.time()
print ('bottomup function took %0.3f ms' % ((time2-time1)*1000.0))
