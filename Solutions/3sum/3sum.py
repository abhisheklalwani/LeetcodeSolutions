'''
# Time Complexity - O(n^2) 
# Space Complexity - O(n^2)
We start with sorting the array.
Once the array is sorted, we fix the first element (nums[0]) and initialize 2 pointers l and r.
l is initialized at i+1, i.e., 0+1=1, and r is initialized at the last element.
Since the array is sorted, it is the least and the max element, respectively.
We then check the sum (three) of nums[i]+nums[l]+nums[r].
If it is greater than 0, we reduce the index r (Since the array is sorted, that reduces the value of threesum).
If it is less than 0, we increase the index l (Since the array is sorted, that increases the value of threesum).
If it is equal to 0, we store the result in an array called result, which we eventually return.
Now, for a given value of i, there can be multiple solutions ([-2,0,2],[-2,-1,3]).
But, the subsequent solutions for a given value of i will lie only in the reduced area of interest, i.e., between the current value of l and r.
Thus, we increase the value of l.
To avoid duplicates, we analyze only those values of l which we haven't already analyzed.
Once we have reached l == r, we increment the value of i and check for duplicates there are well.
'''
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                threesum = nums[i]+nums[r]+nums[l]
                if threesum > 0:
                    r = r-1
                elif threesum < 0:
                    l = l+1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l = l+1
                    while nums[l] == nums[l-1] and l < r:
                        l = l+1
        return result