''' 
Time Complexity - O(n) 
Space Complexity - O(n)
Keep adding all the encountered elements to a hashset, which you can then query to find target-current_value.
If you find a match, just return, since the question specified a unique solution.
Since querying a hashset takes O(1) time, the solution is O(n) in nature.
'''
class Solution(object):
    def twoSum(self, nums, target):
        x = {}
        for i in range(len(nums)):
            if (target - nums[i]) in x:
                return [i,x[target - nums[i]]]
            x[nums[i]] = i