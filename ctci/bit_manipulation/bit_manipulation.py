#!/usr/bin/python


def setbit(bitmap, index):
    mask = (1 << index)
    bitmap = bitmap | mask


def clearbit(bitmap, index):
    mask = ~(1 << index)
    bitmap = bitmap & mask


def getbit(bitmap, index):
    mask = (1 << index)
    return ((bitmap & mask) != 0)

def clear_bits_at_right_of_index(bitmap, idx):
    mask = (1 << idx)

# https://www.willmcgugan.com/blog/tech/post/finding-the-first-bit-set-with-python/
def getbit_index(bitmap):
    int(math.log(bitmap, 2))