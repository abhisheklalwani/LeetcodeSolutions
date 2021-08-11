'''
Time Complexity - O(n) (Here n represent the number of nodes in the tree)
Space Complexity - O(n) (The last layer of the tree will contain n/2 elements, all of which will be in 1 queue)

The main idea which we leverage is that of level order traversal.
We maintain 2 queues.
We keep appending the nodes of 1 level in queue_1.
Then, until queue_1 is empty, we pop nodes out of the queue and append all the children nodes to queue_2.
Then, we reverse the process and we empty out queue_2, while filling all children back in queue_1.
This technique is commonly used for level order traversal.
If we append all the popped out nodes to an array and return it, that will be the level order traversal.
Here, we are just interested in the last node of every level of the tree.
So we just append that to an array and return it.
We start by appending the root node to queue_1.
Then, while one of the queues is non-empty, we check the non-empty queue (at any point at the starting of the loop, one of the queues will be empty).
We first check if queue_1 is not empty.
If it is not empty, we pop out all the elements from the queue_1 and append their children to queue_2.
We similarly check for queue_2 and perform the same process with the roles reversed.
At the end of every sub-loop, we append the last element of the queue to the final array.
We finally return the array.
'''
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        queue_1 = []
        queue_2 = []
        result = [root.val]
        queue_1.append(root)
        while queue_1 or queue_2:
            if queue_1:
                while queue_1:
                    current = queue_1.pop(0)
                    if current.left:
                        queue_2.append(current.left)
                    if current.right:
                        queue_2.append(current.right)
                if queue_2:
                    result.append(queue_2[-1].val)
            if queue_2:
                while queue_2:
                    current = queue_2.pop(0)
                    if current.left:
                        queue_1.append(current.left)
                    if current.right:
                        queue_1.append(current.right)
                if queue_1:
                    result.append(queue_1[-1].val)
        return result