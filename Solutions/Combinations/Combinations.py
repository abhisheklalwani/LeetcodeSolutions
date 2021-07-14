'''
Space Complexity - O(k)
(   
    Max recursion depth - k
    Space taken in 1 call - 1
    O(k*1)
    Not counting the final output array in the space here.
)
We start with an array of [1,n] and we call it the candidates array.
We pick one element from that array and append it to the current_array.
We call backtrack with the updated current_array and in place of candidates, we pass candidates[i+1:].
This ensures 2 things -
1. The current element is not appended more than once in the current_array.
2. The combination is added only once to the final output_array.
As soon as the length of the current_array reaches K, we append it to the output_array.
We repeat the process for every element of the array.
'''
class Solution(object):
    def combine(self, n, k):
        def backtrack(output_array,current_array,candidates,k):
            if len(current_array) == k:
                output_array.append(current_array)
                return
            else:
                for i in range(len(candidates)):
                    if len(candidates[i+1:])+len(current_array)+1>=k:
                        backtrack(output_array,current_array+[candidates[i]],candidates[i+1:],k)
                return
        output_array = []
        backtrack(output_array,[],[i for i in range(1,n+1)],k)
        return output_array
                
                