'''
Time Complexity - O(n) (Here n represent the number of nodes in the smaller tree)
Space Complexity - O(1)

The main idea is that we compare te value of corresponding nodes until we find a node pair in which the values don't match.
If both the nodes in the pair are None, we return True.
If one of them is None, we return False.
If both of them are not None, we check if their values are equal.
If they are, we check if their subTrees are equal.
If not, we return False.
'''
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        else:
            if p!= None and q!=None:
                return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False