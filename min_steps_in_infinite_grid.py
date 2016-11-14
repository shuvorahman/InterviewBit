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
    import math
        
    def distance(self,x1,y1,x2,y2):
        return (x1-x2)**2 + (y1-y2)**2
        
    def move(self,x1,y1,x2,y2):
        dist = self.distance(x1,y1,x2,y2)
        if (x1==x2):
            return abs(y1-y2)
        elif (y1==y2):
            return abs(x1-x2)
        else:
            list = []
            if self.distance(x1,y1-1,x2,y2) < dist:
                list.append(self.distance(x1,y1-1,x2,y2))
            if self.distance(x1,y1+1,x2,y2)< dist:
                list.append(self.distance(x1,y1+1,x2,y2))
            if self.distance(x1+1,y1-1,x2,y2)< dist:
                list.append(self.distance(x1+1,y1-1,x2,y2))
            if self.distance(x1-1,y1-1,x2,y2)< dist:
                list.append(self.distance(x1-1,y1-1,x2,y2))
            if self.distance(x1+1,y1,x2,y2)< dist:
                list.append(self.distance(x1+1,y1,x2,y2))
            if self.distance(x1-1,y1,x2,y2)< dist:
                list.append(self.distance(x1-1,y1,x2,y2))
            if self.distance(x1+1,y1+1,x2,y2)< dist:
                list.append(self.distance(x1+1,y1+1,x2,y2))
            if self.distance(x1-1,y1+1,x2,y2)< dist:
                list.append(self.distance(x1-1,y1+1,x2,y2))
                
            a = min(list)
            list =[]
            
            if a == self.distance(x1,y1-1,x2,y2):
                return 1+self.move(x1,y1-1,x2,y2)
            elif a == self.distance(x1,y1+1,x2,y2):
                return 1+self.move(x1,y1+1,x2,y2)
            elif a == self.distance(x1+1,y1-1,x2,y2):
                return 1+self.move(x1+1,y1-1,x2,y2)
            elif a == self.distance(x1-1,y1-1,x2,y2):
                return 1+self.move(x1-1,y1-1,x2,y2)
            elif a == self.distance(x1+1,y1,x2,y2):
                return 1+self.move(x1+1,y1,x2,y2)
            elif a == self.distance(x1-1,y1,x2,y2):
                return 1+self.move(x1-1,y1,x2,y2)
            elif a == self.distance(x1+1,y1+1,x2,y2):
                return 1+self.move(x1+1,y1+1,x2,y2)
            else:
                return 1+self.move(x1-1,y1+1,x2,y2)
                
    def coverPoints(self, X, Y):
        result = 0
        if len(X) == len(Y):
            if len(X)>1:
                for i in range(len(X)-1):
                    #dist = self.distance(X[i],Y[i],X[i+1],Y[i+1])
                    result += self.move(X[i],Y[i],X[i+1],Y[i+1])
                return result
            elif len(X)==1:
                return 0
            else:
                return None
        return None
            
