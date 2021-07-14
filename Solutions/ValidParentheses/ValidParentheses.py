'''
Time Complexity - O(n) 
Space Complexity - O(n)

We iterate through the characters of the string s.
If we encounter an opening bracket, we add it to the stack.
If we encounter a closing bracket, we try to find a similar opening bracket at the top of the stack.
If we find it, we pop it out of the stack.
If not, we return False.
At the end of this, if the stack is not empty we return False, since that represents some unclosed brackets.
'''
class Solution(object):
    def isValid(self, s):
        stack = []
        opening = ['[','{','(']
        closing = [']','}',')']
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if len(stack)>0 and opening.index(stack[-1]) == closing.index(s[i]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        