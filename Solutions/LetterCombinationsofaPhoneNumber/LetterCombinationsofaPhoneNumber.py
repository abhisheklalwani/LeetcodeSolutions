'''
Time Complexity - O(4^n) (Imagine the input is 999 - There will be 64 combinations).
Space Complexity - O(4^n) (to store the output)
It is a simple recursion problem.
In case of recursion problem, you want to think about 2 aspects - 
1. Recursion Condition
2. Break Condition
The recursion condition is the one which we need to break down further to reach a break condition.
The break condition is the one for which we know the output.
In the example below, the recursion condition is the one where the len(digits) > 1. In that case, we break the condition by calling the function again,
but with the substring of digits containing everything but the first letter.
We keep doing this until we reach our break condition, when len(digits) == 1, for which we know the answer (see mapper below).
The idea is that we get the output for digits[1:] and we feed digits[0] to mapper.
Then, we generate all possible sequences by combining all entries of both the lists.
And we return the same.
'''
class Solution(object):
    def letterCombinations(self, digits):
        mapper = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if len(digits) == 0:
            return []
        return letterRecursive(digits,mapper)

def letterRecursive(digits,mapper):
    if len(digits) == 1:
        return mapper[digits[0]]
    else:
        result = []
        result_recurse = letterRecursive(digits[1:],mapper)
        result_0 = mapper[digits[0]]
        for i in result_recurse:
            for j in result_0:
                result.append(j+i)
        return result