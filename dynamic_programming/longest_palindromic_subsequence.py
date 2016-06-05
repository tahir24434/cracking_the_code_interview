# Find the longest palindrome that is a sub-sequence of a given input string.
# example: AABCDEBAZ
# Longest Palindromic subsequence: ABCBA or ABDBA or ABEBA
# There are many subsequences can be found which are palindrome like, AA, BCB, ABA, BB etc but we need to find the one
# with the maximum length
# https://www.youtube.com/watch?v=_nCsPn7_OgI

def lps(string):
    str_len = len(string)
    # Declare (str_len x str_len) matrix.
    # list of lists: [[0 for x in range(cols_count)] for x in range(rows_count)]
    # LP[i][j] - will used to store length of palindrome from ith index to jth index
    lp = [[0 for x in range(str_len)] for x in range(str_len)]

    # string of length 1 is palindrome of length 1.
    for i in range(str_len):
        lp[i][i] = 1

    # Calculate the number of palindromes in substring of length 2, 3, ... n
    for substr_len in range(2, str_len+1):
        for i in range(0, str_len - substr_len + 1):
            j = i + substr_len - 1
            if string[i] == string[j] and substr_len == 2:
                lp[i][j] = 2
            elif string[i] == string[j]:
                lp[i][j] = 2 + lp[i+1][j-1]
            else:
                lp[i][j] = max(lp[i][j-1], lp[i+1][j])

    return lp[0][str_len-1]


# Driver program to test above functions
seq = "cdabedc"
print("The length of the LPS is " + str(lps(seq)))
