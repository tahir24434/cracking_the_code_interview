#!/usr/bin/python


def setbit(bitmap, index):
    mask = (1 << index)
    return bitmap | mask


def clearbit(bitmap, index):
    mask = ~(1 << index)
    return bitmap & mask


def getbit(bitmap, index):
    mask = (1 << index)
    return ((bitmap & mask) != 0)


def clear_bits_msb_through_idx(bitmap, idx):
    mask = (1 << idx)  # All zeroes except 1 at position idx (idx= 2. 000100)
    mask -= 1  # All zeroes followed by idx 1  (000011)
    return bitmap & mask

# https://www.willmcgugan.com/blog/tech/post/finding-the-first-bit-set-with-python/
def getbit_index(bitmap):
    int(math.log(bitmap, 2))