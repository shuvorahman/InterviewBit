# You are in an infinite 2D grid where you can move in any of the 8 directions :

#  (x,y) to 
#     (x+1, y), 
#     (x - 1, y), 
#     (x, y+1), 
#     (x, y-1), 
#     (x-1, y-1), 
#     (x+1,y+1), 
#     (x-1,y+1), 
#     (x+1,y-1) 
# You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        result = 0
        if len(X) == len(Y):
            if len(X)>1:
                for i in range(len(X)-1):
                    result += max(abs(X[i]-X[i+1]),abs(Y[i]-Y[i+1]))
                return result
            elif len(X)==1:
                return 0
            else:
                return None
        return None