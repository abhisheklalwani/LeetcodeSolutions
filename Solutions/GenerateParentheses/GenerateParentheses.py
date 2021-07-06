'''
Time Complexity - O(4^n) (2 options at every postion - ( or ) and the length of the enire string = 2n. So 2^2n  =4n).
Space Complexity - O(4^n) (to store the output)
Recursion condition -
Maintain the current valid string in a string called current_string.
We also maintain an output_array which contains all the valid strings.
We then decide 2 conditions to maintain the validity of the string.
1. The number of opening brackets should be less than n to add an opening bracket.
2. The number of closing brackets should be less than the number of opening brackets to add a closing bracket.
We maintain the number of opening brackets in left.
We maintain the number of closing brackets in right.
if left < n, we add an opening bracket to the current_string.
if right < left, we add a closing bracket to the current_string.
The idea is as and when a valid string is constructed through the recursion condition, it will be appended to the output array.

Break Condition -
The length of the string should be 2*n.
We have already ensured the validity of string by using the 2 conditions mentioned above.
As soon as the length of the string reaches 2*n, we can add it to the output_array.
And we return the same.
'''
class Solution(object):
    def generateParenthesis(self, n):
        output_array = []
        def backtrack(output_array,current_string,left,right,n):
            if len(current_string) == 2*n:
                output_array.append(current_string)
                return
            if left < n:
                backtrack(output_array, current_string+ '(', left+1, right, n)
            if right < left:
                backtrack(output_array, current_string+ ')', left, right+1, n)
        backtrack(output_array,'',0,0,n)
        return output_array
        