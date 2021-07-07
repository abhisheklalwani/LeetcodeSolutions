'''
Time Complexity - O(n*(2^n)) (You generate 2^n elements and append the new element for the next step).
Space Complexity - O(1) (all in-place modifications, not counting the output array here).

Base/Break Condition -
if len(nums) == 1:
    return the number itself and the empty set
Recursion Condition - 
if len(nums) != 1:
    remove the first element and calculate the superset of the remaining array.
    Now, make a deep copy of this superset and append the first element to one of the copies.
    Concatenate both the copies and return it.
'''
import copy
class Solution(object):
    def subsets(self, nums):
        def backtrack(nums):
            if len(nums) == 1:
                return [[nums[0]],[]]
            else:
                result_recurse = backtrack(nums[1:])
                result_current = copy.deepcopy(result_recurse)
                for i in range(len(result_current)):
                    result_current[i].append(nums[0])
                return result_current+result_recurse
        return backtrack(nums)