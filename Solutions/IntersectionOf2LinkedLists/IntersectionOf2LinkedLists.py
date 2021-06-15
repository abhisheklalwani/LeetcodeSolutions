'''
Time Complexity - O(n) 
Space Complexity - O(1)
There are 2 ways to go about this problem - 
1. You can iterate both the lists and find their respective lengths. You can then start with 2 pointers, 1 for each of the lists 
and increment the pointer on the longer list by the difference in the lengths. Then we can increment the pointers simultaneously
and return the node where both the pointers point to the same node.
2. One other way is to again take 2 pointers. Increment both of them simultaneously until one of them reaches None i.e. the end of the list.
Once a pointer is set to None, initialize it to the head of the other list. Do the same for both the pointers. This way the offset between the 2 list
is accounted for and both the pointers reach the common node simultanrously. 
It is also necessary that the condition should be kept at p == None and not p.next == None.
This way if there is no intersecton of the lists both the pointers will intersect at None, which is the expected output in case of no intersection.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p = headA
        q = headB
        while p!=q:
            if p == None:
                p=headB
            else:
                p=p.next
            if q == None:
                q=headA
            else:
                q=q.next
        return p