# a square root of a number x is a number y such that y^2 = x.


def find_square_root(x, precision=0.0001):
    # The precision must be greater than zero,
    # root must be a positive number
    # assert(precision > 0, str(precision), 'is not a valid value, it must be a positive integer')
    assert x > 0, 'root can not be a negative number'

    lo = 0
    hi = max(x, 1)
    count = 0
    while count < 100:
        y = (lo + hi) / 2
        y_square = y*y
        if abs(y_square-x) <= precision:
            break
        elif y_square < x:
            lo = y
        else:
            hi = y
        count += 1
    print ('Num of iterations:', count, 'Estimate:', y)
    return y

if __name__ == "__main__":
    print (find_square_root(239426782))
