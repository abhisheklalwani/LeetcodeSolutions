'''
Time Complexity - O(n)
Space Complexity - O(n)
We make an array called result which stores the minimum cost to reach i at the ith index.
Now, There are 2 ways to reach any ith index.
Either you come to i-1 and take 1 step, or you reach i-2 and take 2 steps.
The minimum cost to reach i-1 will be result[i-1].
The minimum cost to reach i-2 will be result[i-2].
result[i] will be min(result[i-2]+cost[i-2],result[i-1]+cost[i-1]).
We finally return result[-1], which signifies the minimum cost to reach the top of the stairs. 

'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        result = [0]*(len(cost)+1)
        result[0] = 0
        result[1] = 0
        for i in range(2,len(result)):
            result[i] = min(cost[i-1]+result[i-1],cost[i-2]+result[i-2])
        return result[-1]
        