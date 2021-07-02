''' 
Time Complexity - O(n) 
Space Complexity - O(1)
We need to change every pointer to point to the previous node.
For that node, we need information of the previous node at every node which will be stored in 'head' in our case.
We need the information of the current node which will be stored in the 'current' node.
And we need the information of the next node which is already stored in current.next.
We first initialize current with head.next (after checking head and head.next are not None).
And we point head.next to None since that will be the end of the list eventually.
We then move forward until current is set to None.
We store current.next in incoming and we point current.next to head, thus reversing the link to the previous node instead of next.
We then move forward by initializing the head with the current node and current with the actual next node, which we stored in incoming in the beginning.
We return head at the end.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        current = head.next
        head.next = None
        while current != None:
            incoming = current.next
            current.next = head
            head = current
            current = incoming
        return head
        