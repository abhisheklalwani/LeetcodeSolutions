'''
Time Complexity - 
__init__ -> O(1)
enQueue -> O(1)
deQueue -> O(1)
Front -> O(1)
Rear -> O(1)
isEmpty -> O(1)
isFull -> O(1)

Space Complexity - 
__init__ -> O(1)
enQueue -> O(1)
deQueue -> O(1)
Front -> O(1)
Rear -> O(1)
isEmpty -> O(1)
isFull -> O(1)



'''
class MyCircularQueue(object):
    class ListNode(object):
        def __init__(self,val):
            self.val = val
            self.next = None
    
    def __init__(self, k):
        self.end = None
        self.size = 0
        self.buffer = k
        """
        :type k: int
        We initialize the pointer to the end node of the circular node as None.
        We also initialize the actual size of the list as 0.
        We store the max size of the list k in the variable called buffer.
        """
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        We check if the list is not already at it's max size.
        If it is, we just return False.
        If not, we check if the current size of the list is 0.
        If yes, we initialize end with a new Node containing the passed value.
        The next of end points back to end.
        If the size is not 0, we store the head of the list (end.next) in temp and add a new Node with the passed value at the end of the list.
        We update the end of the list and we make sure the next pointer of the new end points to the old end, thus maintaining the circular property.
        We update the self.size variable as well to indicate the actual size of the list.
        """
        if self.size < self.buffer:
            if self.size == 0:
                self.end = self.ListNode(value)
                self.end.next = self.end
            else:
                temp = self.end.next
                self.end.next = self.ListNode(value)
                self.end = self.end.next
                self.end.next = temp
            self.size+=1
            return True
        else:
            return False
        
    def deQueue(self):
        """
        :rtype: bool
        We want to delete the first element of the circular queue.
        We check if the actual size of the linked list is 0.
        If yes, we just return False.
        Otherwise, we check if the size is 1.
        If yes, we just point end to None.
        Else, we skip the head node, by directly pointing the end to the next of head (end.next) node.
        We update the self.size variable as well to indicate the actual size of the list.
        """
        if self.size > 0:
            if self.size == 1:
                self.end = None
            else:
                self.end.next = self.end.next.next
            self.size-=1
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        We return the value of head, which is the next pointer of self.end. (Assuming the size of the list is not 0)
        """
        if self.size == 0:
            return -1
        else:
            return self.end.next.val
        
    def Rear(self):
        """
        :rtype: int
        We return the value of end. (Assuming the size of the list is not 0)
        """
        if self.size == 0:
            return -1
        else:
            return self.end.val
        
    def isEmpty(self):
        """
        :rtype: bool
        We return True if the size is 0.
        """
        return not bool(self.size)
        
    def isFull(self):
        """
        :rtype: bool
        We return True if self.buffer == self.size.
        """
        return not bool(self.buffer - self.size)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()