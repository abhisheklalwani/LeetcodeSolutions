'''
Time Complexity - O(n)
Space Complexity - O(1)

There are 2 types of extra brackets - 
1. Opening
2. Closing
The basic idea is we identify valid brackets and count all the invalid brackets.
We use a stack to keep track of pairs of brackets.
We also use a count variable which is supposed to count the number of extra closing bracket.
We iterate through the string.
If we find an opening bracket, we directly add it to the stack.
If we find a closing bracketm, we check the top of the stack (assuming there is something in the stack, if not then we just count the current closing bracket as extra).
If there is an opening bracket there, we pop it from the stack and continue forward iterating the string (since that signifies a valid set of parentheses).
If there is not an opening bracket there, we increment the count of the closing brackets as maintained in count. (count+=1)
At the end, stack will contain all the opening brackets which are extra.
count will contain the count of extra closing brackets.
We ust return their sum. (len(stack)+count)

'''
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            if s[i] == ')':
                if len(stack) !=0 and stack[-1] == '(':
                    stack.pop()
                else:
                    count+=1
        return len(stack)+count