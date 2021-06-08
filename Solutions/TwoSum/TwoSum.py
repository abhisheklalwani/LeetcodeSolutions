# Time Complexity - O(n) 
# Space Complexity - O(n)
class Solution(object):
    def twoSum(self, nums, target):
        x = {}
        for i in range(len(nums)):
            if (target - nums[i]) in x:
                return [i,x[target - nums[i]]]
            x[nums[i]] = i