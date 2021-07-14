'''
Time Complexity - O(n*n!) 
(
    T(n) = n*(n-1)! + T(n-1) (Refer to the for loop below)
    T(n) = n! + T(n-1)
    T(n) = 1! + 2! + 3! + 4! + .... + (n-1)! + n!
    T(n) = n*(n!) (Worst case)
)
Space Complexity - O(n*n*n!)
(
    Size of output array - n*n!
    We generate output array - n times (Max call stack)
    Thus n*n*n!
)

We take the string and divide it into 2 parts - 
1. first letter
2. rest of the string
We calculate all the possible permutations for the rest of the string.
Then we take all those permutations and insert our first letter in all the possible positions in those permutations.
For example, if we have [1,2,3], we will take 1 and insert it into all the possible permutations of [2,3] which are [2,3] and [3,2].
So we insert 1 in [2,3] at 3 places - [1,2,3] ,[2,1,3] and [2,3,1].
We do the same with all the other permutations of length n-1 (2 in our case).
We append all the results in an empty output array and return the same.
We keep doing this till we reach case == 1 in which we return [[nums[0]]].
'''
class Solution(object):
    def permute(self, nums):
        def backtrack(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            else:
                result_recurse = backtrack(nums[1:])
                output = []
                current_element = nums[0]
                for i in range(len(result_recurse)):
                    for j in range(len(result_recurse[i])+1):
                        start = result_recurse[i][:j]
                        end = result_recurse[i][j:]
                        output.append(start+[nums[0]]+end)
                return output
        return backtrack(nums)