'''
Time Complexity - O(n) (n being the number of nodes in the tree)
Space Complexity - O(n) (In worst case, there will be n/2 nodes in the stack)

2 solutions - 
1. Recursive
We define a function which takes 2 nodes, left and right.
It first checks the 2 nodes and their values.
If they are both None, we return True.
If only one of them is None, we return False.
If they both have equal values, we call our function on the outside and the inside pairs i.e. the values which need to be same for the tree to be symmetric.
We return and of the 2 results to propagate our result back.
We finally just call isMirror (our defined function) on root.left and root.right.

2. Iterative
The iterative version will feature a stack.
Instead of calling the function recursively for the left and right node, we append them to a stack as a pair.
Then, we pop out the topmost element of the stack and perform the same comparisons as before.
If the element which pops out from the stack is a pair of None, we just continue.
If only one of the elements in the pair is None, we return False.
If both the elements are not None, we check their values.
If they are equal, we append the relevant matching pairs to the stack.
If they are not, we return False.
We keep running this loop until the stack is empty.
We finally return True.

'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left,right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val == right.val:
                inPair = isMirror(left.left,right.right)
                outPair = isMirror(left.right,right.left)
                return inPair and outPair
        return isMirror(root.left,root.right)

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        stack = []
        stack.append((root.left,root.right))
        while stack:
            current = stack.pop()
            if current[0] == None and current[1] == None:
                continue
            if current[0] == None or current[1] == None:
                return False
            if current[0].val == current[1].val:
                stack.append((current[0].left,current[1].right))
                stack.append((current[0].right,current[1].left))
            else:
                return False
        return True