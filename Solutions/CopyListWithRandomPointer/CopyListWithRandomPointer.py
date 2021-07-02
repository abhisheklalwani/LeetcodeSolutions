'''
# Time Complexity - O(n) 
# Space Complexity - O(n)
We initialize current with head. 
We also make a new node with value 0 and we use that to initialize 2 new pointers - head_new and current_new.
head_new -> Head of the new list.
current_new -> Current of the new list.
We keep moving forward until current is None.
While moving forward, we make a new node with the value of the current node and append to the list which is handled with current_new.
We also store a mapping of the old and new node in a dictionary called mapper.
Now, we iterate the newly made list and the old list together and we initialize the randon pointer of the new list by using the mapper.
We take the old random pointer, feed it to the dictionary as a key and we get the corresponding random node in the new list which we intialize in our new list.
One check which we need to do here is that of null nodes. If the random node is None, it should also be None in the new list, which we cannot store in our dictionary.
'''
# Definition for a Node.
class ListNode:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        mapper = dict()
        current = head
        head_new = current_new = ListNode(0)
        while current!= None:
            current_new.next = ListNode(current.val)
            current_new = current_new.next
            mapper[current] = current_new
            current = current.next
        current = head
        current_new = head_new.next
        while current!=None:
            if current.random!=None:
                current_new.random = mapper[current.random]
            else:
                current_new.random = None
            current = current.next
            current_new = current_new.next
        return head_new.next