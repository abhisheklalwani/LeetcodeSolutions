'''
Time Complexity - O(n) (Here n represent the number of nodes in the tree)
Space Complexity - O(n)

We start with checking if root is None. If it is, we return False.
If not, we check if root.left is None.
If it is not, we call the hasPathSum function with root.left and targetSum-root.val and store the result in left.
We do the same with root.right and store the result in right.
We finally check if the root node is a leaf node and targetsum==root.val.
If that is the case, we return True.
We finally return left or right.
Since they both are initialized as False, the only way the function returns true is either if one of them is true or if the current node is a leaf
node with targetSum == root.val, which is what is desired in this question. 
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False
        left = False
        right = False
        if root.left:
            left = self.hasPathSum(root.left,targetSum-root.val)
        if root.right:
            right = self.hasPathSum(root.right,targetSum-root.val)
        if root.left == None and root.right == None and targetSum==root.val:
            return True
        return left or right