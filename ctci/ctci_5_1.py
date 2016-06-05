#!/usr/bin/python

# input: N = 1000000000, M = 10011, i = 2, j = 6
# 1. Clear bits of N (N cleared).
#    Create a mask with ones from MSB:j and i:LSB. Something like 1111110000011
#    N & mask
# 2. Shift M so that it lines up with bits through j to i (M shifted)
#    Left shift M to i bits.
# 3. Merge M and N
#    (N cleared) OR (M shifted)


def updateBits(N, M, i, j):
    # ********* 1. Clear bits of N ***********
    all_ones = int('1111111111111', 2)
    # Create left mask i.e 1111110000000
    left_mask = (all_ones << (j + 1))
    # Create right mask i.e 0000000000011
    right_mask = (all_ones << i) - 1
    # Create final mask
    mask = left_mask | right_mask
    # Clear bits of N
    n_cleared = N & mask

    # ********* 2. Align M ***********
    m_aligned = M << i

    # Merge M and N
    return m_aligned | n_cleared

N = int('10000000000', 2)
M = int('10011', 2)
i = 2
j = 6
merged_num = updateBits(N, M, i, j)
print bin(merged_num)

