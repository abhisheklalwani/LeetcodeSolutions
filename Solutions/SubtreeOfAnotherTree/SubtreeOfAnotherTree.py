'''
Time Complexity - O(m*n) (Here n represent the number of nodes in tree 1 and m represents the number of nodes in tree 2. Since we compare both the trees at every match)
Space Complexity - O(1)

The main idea is that we perform dfs in the main tree and everytime the value of the current node matches the value of the root node of the subtree, we compare all the nodes of the subtree with
all the similar nodes of the tree (assuming the current node in the main tree as the root).
In the code, we first check if the subtree root is None.
If yes, we return True since will always be a subtree of any Tree.
If root is None, and subtree is not, we return false.
Then we call the dfs function (traversal) with the root and subroot.
We check if the root is None.
If yes, we return False since the subroot is not None.
Then we check the value of the roots of both the trees and we also compare the corresponding trees.
If they match, we return True.
If not, we perform the same operations with root.left and root.right.
For checking tree, we first check if any of the nodes (root and subroot) are None.
If both are None, we return True.
Then, If only one of them is None, we return False.
Then we compare the value of both the nodes.
If it is not equal, we return False.
If it is equal, we check the left and the right subtrees by calling isCheckTree on the left and right subtrees. 
'''
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isCheckTree(root,subRoot):
            if root == None and subRoot == None:
                return True
            if root == None or subRoot == None:
                return False
            if root.val != subRoot.val:
                return False
            else:
                return isCheckTree(root.left,subRoot.left) and isCheckTree(root.right,subRoot.right)
        def traversal(root,subRoot):
            if root ==  None:
                return False
            if root.val == subRoot.val and isCheckTree(root,subRoot):
                return True
            else:
                return traversal(root.left,subRoot) or traversal(root.right,subRoot)
        if subRoot == None:
            return True
        if root == None:
            return False
        return traversal(root,subRoot)