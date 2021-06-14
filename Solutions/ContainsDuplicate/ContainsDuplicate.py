'''
# Time Complexity - O(n) 
# Space Complexity - O(n)
Check if an element already exists in the set.
If it does not exist, add it in the set.
If the element already exists, return True.
If you reach the end of the array, return False.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        occurence = set()
        for i in nums:
            if i in occurence:
                return True
            else:
                occurence.add(i)
        return False