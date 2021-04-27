import random
import numpy as np  # only required to print the table formatted in 2D on line 65

# toy problem for development purposes
A = "bd"
B = "abcd"

# create longer strings with random letters, for testing
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
seq3 = ''.join(random.choice(alphabet) for _ in range(100))
seq4 = ''.join(random.choice(alphabet) for _ in range(100))
print(seq3)
print(seq4)


# top-down approach (starts from beginning of strings)
def LCS(i, j):
    if i > (len(A) - 1) or j > (len(B) - 1):
        return 0
    elif A[i] == B[j]:
        return 1 + LCS(i + 1, j + 1)
    else:
        return max(LCS(i + 1, j), LCS(i, j + 1))


# print(LCS(0, 0))


# time complexity of 2^n
# bottom-up approach (starts from back of strings)
def lcs_recursive(seq1, seq2, len1, len2):
    # if a string is empty, lcs is 0
    if len1 == 0 or len2 == 0:
        return 0
    # check the two last letters, if the same then +1 and run the function again to check the next letters from behind
    elif seq1[len1 - 1] == seq2[len2 - 1]:
        return 1 + lcs_recursive(seq1, seq2, len1 - 1, len2 - 1)
    # go back one letter in each string for both and run function again
    return max(lcs_recursive(seq1, seq2, len1 - 1, len2), lcs_recursive(seq1, seq2, len1, len2 - 1))


# print(lcs_recursive(A, B, len(A), len(B)))
# print(lcs_recursive(seq3, seq4, len(seq3), len(seq4)))


# import time # used for timing the functions. move to above the function u want to test, remember to also move the print statement below the function
# start_time = time.time()


# @profile  # used for the memory_profiler module. move to above the function u want to test
def lcs_dynamic(seq1, seq2, len1, len2):
    table = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):  # skips row and column 0 in the table since its i-1 anyway later
            # if i == 0 or j == 0:  # keep the first row and column at 0
            #     # pass
            #     table[i][j] = 0
            if seq1[i - 1] == seq2[j - 1]:  # if the two letters are the same
                table[i][j] = table[i - 1][j - 1] + 1  # increase by 1
            else:  # set current pos equal to max of its two diagonal neighbors
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    print(np.array(table))  # making it into a numpy ndarray for nicer printing
    return table[len1][len2]


# print(lcs_dynamic(A, B, len(A), len(B)))
print(lcs_dynamic(seq3, seq4, len(seq3), len(seq4)))

# print("--- %s seconds ---" % (time.time() - start_time)) # used for timing functions, move to below function call
