'''
Time Complexity - O(n) (Here n represent the number of nodes in tree)
Space Complexity - O(1)

The main idea is that the value of root should lie between a specified threshold to maintain the BST property.
The main root (with which we start) should lie between +infinity and - infinity.
Then, for the left subtree, the value of root should lie between -infinity and root.val (Here root.val signifies the value of main root).
Similary for the right subtree, the value of root should lie betwenn root.val and +infinity.
We call this function recursively. Everytime we go to a left subtree, we update the max threshold since all the values in the left subtree need to be less than root.val.
Similarly, Everytime we go to a right subtree, we update the min threshold since all the values in the right subtree need to be greater than root.val.
If the root is None, we return True.
If the root is not None, we check if the value of root lies between the min and the max threshold.
If yes, we check if the left and right subTrees are valid BSTs. We return an and of the 2 subtrees.
If not, we return False.
In the main function, we call checkRoot with -infinity and +infinity.
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkRoot(root,minThresh,maxThresh):
            if root == None:
                return True
            else:
                if root.val > minThresh and root.val < maxThresh:
                    return checkRoot(root.left,minThresh,root.val) and checkRoot(root.right,root.val,maxThresh)
                else:
                    return False
        return checkRoot(root,float('-inf'),float('inf'))