'''
We design the backend of a linked list in this question.
init method() -> We have 2 variables - head and size. head is the head node and size is the size of the list. Size is not a necessary variable but a useful one.

get(index) -> First we check whether the given index is valid i.e. index > 0 and index < self.size. If yes, we move forward the current pointer (initialized with head)
and we keep doing so until we reach the index.

addathead(val) -> addatindex(0,val)

addattail(val) -> addatindex(0,self.size)

addatindex(index,val) -> First we check the validity of the given index. Then, given that the index is valid, we check if the index is 0 or not. Index = 0 is a special
case since that involves changing the head. 
If index==0, we change the head to our new node and the next of new node is set to the previous head.
If index != 0, we move to the parent pointer of index position and insert our node there.
We increment the size in both the cases.

deleteAtIndex(index) -> We check the validity of index first.
Once we have ensured that the index is valid, we check if index==0.
If index == 0, move head to the next node.
If index !=0, we move to the parent node of the index node and skip the index node.
We decrement the size in both the cases.
'''
class MyLinkedList(object):
    class ListNode(object):
        def __init__(self,val):
            self.val = val
            self.next = None
    
    # Time Complexity - O(1) 
    # Space Complexity - O(1)
    def __init__(self):
        self.head = None
        self.size = 0
        """
        Initialize your data structure here.
        """
    # Time Complexity - O(n) 
    # Space Complexity - O(1)
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index <0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    # Time Complexity - O(1) 
    # Space Complexity - O(1)
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)

    # Time Complexity - O(n) 
    # Space Complexity - O(1)
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)

    # Time Complexity - O(n) 
    # Space Complexity - O(1)
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size or index<0:
            return
        current = self.head
        new_Node = ListNode(val)
        if index == 0:
            new_Node.next = current
            self.head = new_Node
            self.size+=1
        else:
            for _ in range(index-1):
                current = current.next
            new_Node.next = current.next
            current.next = new_Node
            self.size+=1

    # Time Complexity - O(n) 
    # Space Complexity - O(1)
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        current = self.head
        if index == 0:
            self.head = self.head.next
            self.size-=1
        else:
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
            self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)