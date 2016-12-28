import bit_manipulation
sequence_length = 32


def flip_bit_to_win(num):
    """ Flip a bit and win!!!!!! """
    """ Convert to binary """
    binary = int(num, 2)
    current = 0
    last = 0
    longest = 0
    for i in range(sequence_length):
        bit = bit_manipulation.getbit(binary, i)
        if bit:
            current += 1
            longest = max(longest, current + last + 1)
        else:
            last = current
            current = 0
    return longest

print (flip_bit_to_win("1110010"))  # => 4
print (flip_bit_to_win("0001101"))  # => 4
print (flip_bit_to_win("0100001"))  # => 2
print (flip_bit_to_win("0101011"))  # => 4
print (flip_bit_to_win("0101100"))  # => 4
