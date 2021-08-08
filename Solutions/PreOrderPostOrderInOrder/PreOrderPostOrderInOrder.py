'''
Time Complexity - O(n) (n-> number of nodes in the tree)
Space Complexity - O(n) (In worst case, all the nodes of the tree will be in the stack)
2 solutions for any order of traversal, Iterative and Recursive.
1. The recursive solution is pretty straightforward. We call the function on the right and the left node of the root recursively and append self.root at the appropriate location.
This approach will remain same even for all the other traversals. Just the order of appending self.root will change depending upon the exact traversal.

2. The iterative solution of all the traversals uses stacks. The main idea is that you append the nodes which are supposed to come before the root in the stack so that when items
are popped out of the stack, the order is maintained.
For example, in Pre-order, we start by appending root to the stack. Then, while the stack is not empty, we pop the root node from the stack.
We append it to the result array, which is what we plan to return finally.
Then, we first check the right node of the root, and if it is not empty, we append it to the stack.
We do the same for the left sub node as well.
We pick right first because we want left to be included first in the final array. Since we are working with a stack which reverses the order, we check the right node first.

We apply a similar strategy for In-order traversal as well.
We start by appending the root to a stack.
Then, while the stack is not empty, we check the topmost element of the stack without popping it. If the left of the topmost element is not None, we append it to the stack and
break the connection (make left None) to avoid an infinite loop.
If the left is None, we pop the element out of the stack and append to the result array.
Then, we check for the right of the element. If it is not None, we append it to the stack and proceed in the same manner.

We again apply a similar strategy for post-order traversal as well.
We first append the root node to a stack.
Then, while the stack is not empty, we first check the right node of the topmost element of the stack without popping it.
If it is not empty, we append it to the stack and break the connection (make right None) to prevent infinite loops.
Then we check the left of the same root Node, which is now the second topmost element in the stack.
If that is also not None, we append it to the stack and break the connection (make Left None) to prevent infinite loops.
If the right node of the topmost Node is None, we check for the left node of the topmost root node in the stack.
If that is not None, we append it the stack and break the connection as before.
If both are None, we just pop the node from the stack and append it's value to the final result array.

We finally return the result array in all the cases.
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return [self.root]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        else:
            return []

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        result = []
        if root!=None:
            queue.append(root)
        while queue:
            current = queue.pop()
            result.append(current.val)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return result

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.inorderTraversal(root.left)+[self.root]+self.inorderTraversal(root.right)
        else:
            return []

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        if root == None:
            return []
        result =[]
        stack.append(root)
        while stack:
            if stack[-1].left != None:
                stack.append(stack[-1].left)
                stack[-2].left=None
            else:
                current = stack.pop()
                result.append(current.val)
                if current.right != None:
                    stack.append(current.right)
        return result

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[self.root]
        else:
            return []

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if root == None:
            return []
        stack.append(root)
        while stack:
            if stack[-1].right != None:
                stack.append(stack[-1].right)
                stack[-2].right = None
                if stack[-2].left != None:
                    stack.append(stack[-2].left)
                    stack[-3].left=None
            else:
                if stack[-1].left != None:
                    stack.append(stack[-1].left)
                    stack[-2].left = None
                else:
                    current = stack.pop()
                    result.append(current.val)           
        return result