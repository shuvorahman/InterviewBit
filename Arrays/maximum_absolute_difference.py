# Maximum Absolute DifferenceBookmark Suggest Edit
# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# For example,

# A=[1, 3, -1]

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        if len(A)==0:
            return 1
        elif len(A)==1:
            return 0
        else:
            array_1 = []
            array_2 = []
            result = 0
            for i in range(len(A)):
                array_1.append(A[i] + i)
                array_2.append(A[i] - i)
            return max(max(array_1)-min(array_1),max(array_2)-min(array_2))