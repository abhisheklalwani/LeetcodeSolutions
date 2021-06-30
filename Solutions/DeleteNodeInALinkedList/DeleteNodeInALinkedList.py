'''
# Time Complexity - O(n) 
# Space Complexity - O(1)
The question is slightly misleading in nature.
While the questions asks to delete a node, it is theoretically not possible to delete a node without knowing it's parent node.
Since the head node or any previous node is not given, we can not actually delete the node.
Rather we replace the value in the node, by the value of the next node, and we keep doing this till the end of the list.
When we reach the second-last node, we take up the value of the last node and we point the next of that node to none.
'''
class Solution(object):
    def deleteNode(self, node):
        while node.next.next != None:
            node.val = node.next.val    
            node = node.next
        node.val = node.next.val
        node.next = None
        return