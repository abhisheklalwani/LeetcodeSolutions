''' 
Time Complexity - O(n) 
Space Complexity - O(1)
Have 2 pointers in the list, both initialized at head.
Move pointer_1 one step at a time.
Move pointer_2 2 steps at a time.
If they ever are equal, there is a cycle in the list.
Otherwise, one of them will go none and we can return false then.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        pointer_1 = head
        pointer_2 = head
        while pointer_1 != None and pointer_2 != None and pointer_2.next != None:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
            if pointer_1 == pointer_2:
                return True
        return False