'''
Time Complexity - O(n) 
Space Complexity - O(1)
The trick here is to initialize 2 pointers.
First pointer stays at head.
We move forward the second pointer n spaces.
Then we move both pointers forward till the second pointer reaches the end of the linked list.
At this moment, the first pointer is pointing to the node which is just before the one to be deleted.
We check if first.next == None, which can be a possible corner case.
If that's not the case, we simply skip the next node by first.next = first.next.next.
We return the head of the list as requested.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        first = head
        second = head
        while n>0 and second.next!=None:
            second = second.next
            n-=1
        if n!=0: #This means n is 1 which means we want to delete the first node of the list.
            return first.next
        while second.next != None:
            second = second.next
            first = first.next
        if first.next == None:  #This will happend when there is only one node in the list. We delete that and return None.
            return None
        else:
            first.next = first.next.next
        return head   