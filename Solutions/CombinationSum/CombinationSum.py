'''
Time Complexity - O(2^n) (You generate all possible combinations and check whether they sum up to target).
Space Complexity - O(target/min(candidates)) (For recursion problem, the space complexity is determined by the maximum recursion depth multiplied by the
memory taken by 1 call. Max recursion depth will be achieved when you try to generate the target by minimum element again and again. Memory taken by 1 call
is O(1) since no new variable is initialized).

Base/Break Condition -
If target < 0:
    Given that all candidates are >=1, we can safely return from here.
If target == 0:
    Here the current list can be appended to the final output array which will be returned.

Recursion Condition - 
Take one entry from the candidate and call backtrack with target - entry and current_list+[entry].
Also, make sure that you call backtrack with the updated list of candidates (candidates[i:]) to avoid repeats. ([2,3] for target 5 and not [2,3] and [3,2])
When target reaches 0, we can safely add the current_list to output_array.
When target reaches < 0, we can safely disregard that current list and return (check break condition above).
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(output_array,current_list,candidates,target):
            if target < 0:
                return
            if target == 0:
                output_array.append(current_list)
                return
            else:
                for i in range(len(candidates)):
                    backtrack(output_array,current_list+[candidates[i]],candidates[i:],target-candidates[i])
        output_array = []
        backtrack(output_array,[],candidates,target)
        return output_array