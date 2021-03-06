import bit_manipulation
sequence_length = 32


def next_number(num):
    bin_str = bin(num)
    bin_num = int(bin_str, 2)
    idx_of_right_most_non_trailing_zero = get_idx_of_right_most_non_trailing_zero(bin_num)
    number_of_ones_before_right_most_non_trailing_zero = get_number_of_ones_before_right_most_non_trailing_zero(bin_num)

    # Set idx bit
    bin_num = bit_manipulation.setbit(bin_num, idx_of_right_most_non_trailing_zero)
    # Clear all bits after idx bit
    all_zeroes_followed_by_idx_ones = (1 << idx_of_right_most_non_trailing_zero) - 1
    all_ones_followed_by_idx_zeroes = ~all_zeroes_followed_by_idx_ones
    bin_num &= all_ones_followed_by_idx_zeroes
    # Set least significant (number_of_ones_before_right_most_non_trailing_zero - 1) bits
    mask = (1 << (number_of_ones_before_right_most_non_trailing_zero - 1)) - 1  # Number of p-1 zeroes followed by ones
    return bin_num | mask


def get_idx_of_right_most_non_trailing_zero(bin_num):
    prev = 0
    for i in range(sequence_length):
        bit = bit_manipulation.getbit(bin_num, i)
        if bit == 0 and prev == 1:
            return i
        elif bit == 1:
            prev = 1

    return -1


def get_number_of_ones_before_right_most_non_trailing_zero(bin_num):
    prev = 0
    number_of_ones = 0
    for i in range(sequence_length):
        bit = bit_manipulation.getbit(bin_num, i)
        if bit == 0 and prev == 1:
            return number_of_ones
        elif bit == 1:
            prev = 1
            number_of_ones += 1

    return -1

# print (get_idx_of_right_most_non_trailing_zero(int("100111010", 2)))
# print (get_number_of_ones_before_right_most_non_trailing_zero(int("100111010", 2)))
print (next_number(5))

