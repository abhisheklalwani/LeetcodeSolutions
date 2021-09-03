'''
Time Complexity - O(n) (n->maximum of days)
Space Complexity - O(n)
We make an empty array with 0s called the result with it's length being the maximum of days + 1. (days is sorted in ascending order).
We then make a set of days for quick retrieval.
We then iterate through our result array.
If the current index is not in days_set, result[i] is simply initialized to result[i-1] (Since there is no travelling on this day, the cost remains the same).
If the current index is in days_set, result[i] can be initialized in 3 ways.
result[i] = result[i-1]+costs[0]
result[i] = result[i-7]+costs[1]
result[i] = result[i-30]+costs[2]
Since we want to maintain the minimum cost, we choose the minimum of the 3 options.
We make sure that the options are valid by checking the validity of the previous index value (i-1,i-7 and i-30 should be greater than 0).
1 question which might come is how do we factor in the validity of an existing pass on a previous day.
That is handled by going back 7/30 days in the past and checking if buying a pass then works for today.
This ensures that only the passes which are in the range of the current date are checked properly.
'''
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        result = [0]*(days[-1]+1)
        days_set = set(days)
        for i in range(len(result)):
            if i not in days_set:
                result[i] = result[i-1]
            else:
                result[i] = min(result[max(0,i-1)]+costs[0],result[max(0,i-7)]+costs[1],result[max(0,i-30)]+costs[2])
        return result[-1]
        