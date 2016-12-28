# Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
# Example:
# input:        29 (11101), 15 (01111)
# output:       2


# odd number will always have 0th bit set.
def num_bits_to_flip(a, b):
    x = a ^ b
    count = 0
    while x != 0:
        count += (x % 2)
        x >>= 1
    return count

if __name__ == "__main__":
    a = 29
    b = 15
    print (bin(a))
    print (bin(b))
    print (num_bits_to_flip(a, b))
    a = 97
    b = 95
    print (bin(a))
    print (bin(b))
    print (num_bits_to_flip(a, b))