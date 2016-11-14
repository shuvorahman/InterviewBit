# Given an array of integers, sort the array into a wave like array and return it, 
# In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

# Example

# Given [1, 2, 3, 4]

# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
#  NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 
# So, in example case, you will return [2, 1, 4, 3] 
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        result = []
        A.sort()
        while True:
            length = len(A)
            if length == 0:
                return result
            elif length == 1:
                result.append(A[0])
                return result
            else:
                temp = A[0:2]
                result.append(temp[1])
                A.remove(temp[1])
                result.append(temp[0])
                A.remove(temp[0])