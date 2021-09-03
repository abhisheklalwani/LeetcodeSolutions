'''
Time Complexity - O(n)
Space Complexity - O(n)
Number of distinct ways to reach n will be the number of distinct ways to reach n-1 followed by taking 1 step and the number of
distinct ways to reach n-2 followed by taking 2 steps. Consequently, result[n] = result[n-1]+result[n-2].
Result is the array in which we store the number of distinct ways to reach i at the ith index.
We populate the result array all the way till n, starting at 0.
We finally return result[n].

'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0]*(n+1)
        result[0] = 1
        result[1] = 1
        for i in range(2,n+1):
            result[i] = result[i-1]+result[i-2]
        return result[n]