'''
Time Complexity - O(m) (Here m is the size of the output).
Space Complexity - O(m)

The idea behind this problem is to focus on the occurence of ']' in the given string.
We initialize an empty string and we use it as a stack.
We then iterate through the characters of the string s.
As long as the character is not ']', we keep inserting the characters into the stack.
If we encounter a ']', we do 2 things - 
1. We try to get the string enclosed within the '[]' of which we have encountered the ']'. We do this by going back until we encounter '['. We also keep removing all these from the stack.
We store this reversed string in the 'current' variable.
2. We try to get the count corresponding to this string. We do this by first skipping the '[' and then reading the string just outside the bracket '[' until it stops being a number.
We also keep removing all this from the stack.
We then reverse the count and the current string and generate the final string by multilpying the count with the current string.
We insert the final string back into the stack.
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ''
        for i in range(len(s)):
            if s[i] != ']':
                stack += s[i]
            else:
                current = ''
                while stack[-1] != '[':
                    current += stack[-1]
                    stack = stack[:-1]
                stack = stack[:-1] #skipping the '['
                count = ''
                while len(stack)>0 and stack[-1] in "0123456789": 
                    count += stack[-1]
                    stack= stack[:-1]
                count = count[::-1]
                stack += int(count)*current[::-1]
        return stack
        