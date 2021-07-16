'''
Time Complexity - 
init - O(1)
push - O(1)
pop - O(1)
peek - O(1)
empty - O(1)

Space Complexity -
init - O(1)
push - O(1)
pop - O(1)
peek - O(1)
empty - O(1)

init ->
We initialize the empty stack which we call array.

push ->
We check the current minimum of the stack.
If the length of the current array is 0 or if the currnet minimum of the array is greater than val, we append (val,val) to the array.
Else, we append(val,currentMinimum) to the array.
The idea is that with every incoming value, we also keep track of the minimum value of the array and append the same to val before appending it to the array.

pop ->
Straight forward pop.

top ->
Straightforwar peek. We refer to the 0th index since we are interested in the element and not the minimum element.

getMin ->
If the size of array is 0, we return None.
Otherwise, we return the minimum_element ([1] index) corresponding to the topmost element of the array.

'''
class MinStack(object):

    def __init__(self):
        self.array = []
        
    def push(self, val):
        if self.getMin() > val or len(self.array) == 0:
            self.array.append((val,val))
        else:
            self.array.append((val,self.getMin()))
    
    def pop(self):
        self.array.pop()

    def top(self):
        return self.array[-1][0] 
        
    def getMin(self):
        if not len(self.array):
            return None
        else:
            return self.array[-1][1]