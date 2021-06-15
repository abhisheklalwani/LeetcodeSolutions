'''
Time Complexity - O(m+n) (m and n are lengths of the 2 lists)  
Space Complexity - O(1)
First check if any of the list is None. If yes, just return the other list.
Then check the first nodes of both the lists and initialize a new pointer (current) with the node which has a lesser value.
Move l1 to the next node in the list or l2 to the next node in the list depending upon which is less.
Store the starting value in a pointer called start which will eventually be returned.
Now, iterate over both the lists using the 2 pointers.
Identify the minimum value and append it to the our current pointer.
Keep doing this until one of the pointers reach the end of the list.
Then append the remaining list to our current pointers.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            current = l1
            l1 = l1.next
        else:
            current = l2
            l2 = l2.next
        start = current
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
            else:
                current.next = l2
                l2 = l2.next
                current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return start