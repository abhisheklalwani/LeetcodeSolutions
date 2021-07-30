'''
Time Complexity - O(n*sqrt(n)) (Number of squares less than n will be sqrt(n))
Space Complexity - O(n) (result array is longer than squares array and is thus the limiting factor)

We solve this using Dynamic Programming.
We initialize an array of length n+1 with 0s.
The i'th element in this array is supposed to contain the least number of perfect squares that sum to i.
So if i is a perfect square, we initialize result[i] as 1.
We check if i is a perfect square by squaring the int of the sqrt(i) and comparing it with i.
If they are equal, i is a perfect square.
We also add i to the squares array and then we continue.
If i is not a perfect square, we check all the spots of result[i-square] where square is an element of the squares array.
We select the minimum of them and initialize result[i] with result[i-square]+1. (result[i-square] is the minimum here).
We finally return result[n].
'''
from math import sqrt
class Solution(object):
    def numSquares(self, n):
        result = [10000]*(n+1)
        squares = []
        for i in range(1,n+1):
            if int(math.sqrt(i))**2 == i:
                squares.append(i)
                result[i] = 1
                continue
            for square in squares:
                if result[i-square]!=0 and result[i-square] + 1 < result[i]:
                    result[i] = result[i-square]+1
        return result[n]