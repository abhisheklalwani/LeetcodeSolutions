'''
Time Complexity - O(n) 
Space Complexity - O(1)
Increment the last digit if it's not 9
If it is 9, make it 0 and move on to the second last digit and so on.
If they are all 9, make them all 0 and append a 1 to the starting of the array.
'''
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
        if digits[0] == 0:
            return [1]+digits