'''
Time Complexity - O(m*n) (m-> number of coins,n->amount)
Space Complexity - O(n)
We make an array called result which stores the fewest number of coins needed to make up i at the ith index.
We fill every index with maximum number of coins required, which will happen if the amount is 10000 (upper-limit) and only possible coin is 1.
The value in that case will be 10000.
We fill index 0 with 0 since 0 coins are required to reach the figure 0.
Now, for every index, we check all the possible coins.
If the current value - the value of coin is >= 0, this means there is valid combination of coins which reaches till i-coin and then, by using coin,
we can reach i. If this combination yields lesser number of coins than the current value of result[i], we replace result[i] with this lesser number of coins.
We do this for every index with every possible coin value.
If the value at the last index of the result array is still at 10000, there is no way to reach the value specified by the last index.
Thus, we return -1.
Else, we return the value at the last index of the result array. 
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = [10000]*(amount+1)
        result[0] = 0
        for i in range(1,len(result)):
            for coin in coins:
                if i-coin >= 0 and result[i-coin]+1 < result[i]:
                    result[i] = result[i-coin]+1
        if result[-1] == 10000:
            return -1
        else:
            return result[-1]
        