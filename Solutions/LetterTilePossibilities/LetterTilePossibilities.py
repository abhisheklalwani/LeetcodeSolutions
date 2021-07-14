'''
Time Complexity - O(2^n) (Since we try all the combinations of all the letters and see what's valid and what not)
Space Complexity - O(n)
(   
    Max recursion depth - n (length of the tiles string)
    Space taken in 1 call - 1
    O(k*1)
    Not counting the final output array in the space here.
)
We start with the tiles string and call it the candidates string.
We pick one element from that string and append it to the current_string.
We call backtrack with the updated current_string and in place of candidates, we pass candidates[:i]+candidates[i+1:], since we are allowed to use the current element only once.
This ensures that the current element is not appended more than once in the current_string.
We repeat the process for every element of the string.
We add all the valid strings (length!=0) to an output set.
We finally return the length of the output set.
'''
class Solution(object):
    def numTilePossibilities(self, tiles):
        output_set = set()
        backtrack(output_set,'',tiles)
        return len(output_set)
        
def backtrack(output_set,current_string,candidates):
            if current_string not in output_set: #If the current_string is already in output_set, all the subsequent combinations are already tried and added to the set.
                if len(current_string) != 0: 
                    output_set.add(current_string)
                for i in range(len(candidates)):
                    backtrack(output_set,current_string+candidates[i],candidates[:i]+candidates[i+1:])
                
                