'''
# Time Complexity - O(log n) 
# Space Complexity - O(log n)
Basically we modify the traditional Binary Search algorithm to look for something more than a direct comparison with a target value.
Our condition now becomes that the current value should be equal to the target value and the value just previous to the current value should not be equal
to the target value, while searching for the start index of the target value.
Similary we also search for the end index.
We modify our recursion conditions to suit our new search criteria.
We also check for corner conditions while checking for the start and end index, if the start index is 0 or the end index is len(nums)-1.
'''
class Solution(object):
    def searchRange(self, nums, target):
        return [startIndex(nums,target,0, len(nums)-1),endIndex(nums,target,0, len(nums)-1)]
def startIndex(nums,target,l,r):
    if r>=l:
        mid = (l+r)/2
        if (mid>0 and nums[mid] == target and nums[mid-1] != target) or (mid == 0 and nums[mid] == target):
            return mid
        elif nums[mid] >= target:
            return startIndex(nums,target,l,mid-1)
        else:
            return startIndex(nums,target,mid+1,r)
    else:
        return -1

def endIndex(nums,target,l,r):
    if r>=l:
        mid = (l+r)/2
        if (mid<len(nums)-1 and nums[mid] == target and nums[mid+1] != target) or (mid == len(nums)-1 and nums[mid] == target):
            return mid
        elif nums[mid] <= target:
            return endIndex(nums,target,mid+1,r)
        else:
            return endIndex(nums,target,l,mid-1)
    else:
        return -1