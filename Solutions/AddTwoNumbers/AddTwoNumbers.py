'''
# Time Complexity - O(n) (n =  Length of the longer list of the 2) 
# Space Complexity - O(n)
The basic idea is simple addition.
You have 2 digits, you add them, add the carry and check if the value is >= 10. If yes, you make carry for the next step 1 and initialize the current
digit with the remainder.
You keep moving forward till both the lists are not none.
If one of the list goes none, you continue the same process with the remaining list (You don't add the value from the other list since it is None now).
If carry !=0 finally, you add a 1 to the end of the list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = current = ListNode()
        carry = 0
        while l1!=None and l2!=None:
            current_val = l1.val+l2.val+carry
            if current_val >= 10:
                carry = 1
                remainder = current_val%10
            else:
                carry = 0
                remainder = current_val
            current.next = ListNode(remainder)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        if l1!=None:
            while l1!=None:
                current_val = l1.val+carry
                if current_val >= 10:
                    carry = 1
                    remainder = current_val%10
                else:
                    carry = 0
                    remainder = current_val
                current.next = ListNode(remainder)
                current = current.next
                l1 = l1.next
        if l2!=None:
            while l2!=None:
                current_val = l2.val+carry
                if current_val >= 10:
                    carry = 1
                    remainder = current_val%10
                else:
                    carry = 0
                    remainder = current_val
                current.next = ListNode(remainder)
                current = current.next
                l2 = l2.next
        if carry!=0:
            current.next = ListNode(1)
        return head.next
        