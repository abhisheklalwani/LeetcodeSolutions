'''
Time Complexity - O(log(n)) approximately - Refer to the complexity analysis here - https://leetcode.com/problems/happy-number/solutions/421162/happy-number/?envType=study-plan&id=level-2.
Space Complexity - O(log(n)) approximately

Fairly simple question.
We define a helper method to create next number from the current number, simplt by extracting it's digits repeatedly and summing them up.
We finally return the result variable from the helper method.
To make sure we don't go into a cycle we keep a visited set of all the number which we have ecnountered up till now.
If n==1, we return True.
If we encouter a visited number, we break the loop and return False.

'''
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = nextNode(n)
            if n ==1:
                return True
        return False

def nextNode(n):
    result = 0
    while n > 0:
        extract_num = n%10
        n = int(n/10)
        result += (extract_num**2)
    return result