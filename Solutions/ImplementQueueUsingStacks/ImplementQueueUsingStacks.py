'''
Time Complexity - 
init - O(1)
push - O(1)
pop - O(n) worst case
peek - O(n) worst case
empty - O(1)

Space Complexity -
init - O(1)
push - O(1)
pop - O(n)
peek - O(n)
empty - O(1)

init ->
We initialize both the stacks as empty lists and size to 0.

push ->
We just append to s1 and increment the size.

pop ->
The idea is that at every pop, you should pop out all elements from s1, put them into s2, pop out the topmost element from s2 and put all the elements back into s1 in the reverse order.
The above idea is right, except that you don't need to put all the element back in s1.
You can just leave the elemnts in s2 and keep returning them when someone calls peek and pop.
There is no use for them back in s1, where we will keep adding new elements.
Also, don't forget to decrement the size.
That brings down the amortized time complexity to O(1).
(You can ditch the size variable if you want, it's just cleaner design)

peek ->
Same as pop, just that instead of popping out element from s2 we just return the topmost element from s2.

empty ->
Check size and return accordingly.
'''
class MyQueue(object):

    def __init__(self):
        self.size = 0
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)
        self.size+=1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.s2) == 0:
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
            self.size-=1
            return self.s2.pop()
        else:
            self.size-=1
            return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.s2) == 0:
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not(self.size)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()