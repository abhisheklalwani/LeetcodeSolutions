'''
2 Solutions - 

1.Using Priority Queue
    Time Complexity - O(k*n*logk) 
        (There are 2 things happening here - 
            1. Visiting each element and adding it to the priority queue (n*k) (n = maximum number of elements in a single list)
            2. extracting all those elements from the priority queue -log k for every element since at any time there are only k elements
            in the priority queue)
    Space Complexity - O(k)
You first start by adding the head nodes of all the lists in the priority queue.
The priority is defined by taking the values stored in the head nodes of the list.
Then, while the list is non-empty, we keep extracting elements from the list one-by-one based on their priority. (log K for priority queues)
We append the extracted element to our final list which we initialize with a 0 value node.
Then we check if the extracted node from the priority queue had a valid next element.
If yes, we append that to the priority queue with the priority specified by the value as before.
We keep doing this until the queue is empty.
'''
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        head = ListNode(0)
        current = head
        pq = PriorityQueue() 
        for node in lists:
            if node:
                pq.put((node.val,node))
        while pq.qsize()>0:
            current.next = pq.get()[1]
            current = current.next
            if current.next:
                pq.put((current.next.val,current.next))
        return head.next
'''
2.Using Arrays and Sorting
    Time Complexity - O(k*n*log(n*k)) 
    Space Complexity - O(n*k)
Simply add all the elements of all the lists in an array.
Sort the array.
Create a list out of those elements in the sorted order.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        values = []
        for head in lists:
            while head!=None:
                values.append(head.val)
                head=head.next
        values.sort()
        head = current = ListNode(0)
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return head.next