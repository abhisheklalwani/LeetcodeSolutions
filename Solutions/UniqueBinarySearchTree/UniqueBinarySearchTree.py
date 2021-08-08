'''
Time Complexity - O(n^2) 
Space Complexity - O(n)

Simple DP Question.
The main idea is that while creating a unique BST with n nodes, we first need to select the root of the tree.
We have n options for that.
Once we have selected a root, since this is a BST we know all the values less than n will lie in the left subtree.
All the values greater than n will lie in the right subtree.
The number of unique trees possible with this root will be a product of the number of unique trees in the left subtree and the number of unique trees in the right subtree.
We start with 0 and keep calculating the number till n.
In the code, we first initialize an array with 0s.
Then, for every value from 0 to n, we calculate the number of unique BSTs using the trick mentioned above.
We know the value of 0 and 1 will be 1.
For 2 and greater, we select nodes from 0 to i-1 as root.
And we add the product of result[j] and result[i-1-j] to result[i] (i-1 because 1 node is used up for root).
We do this for all values till n.
We finally return result[n].
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0]*(n+1)
        result[0] = 1
        result[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                result[i] += result[j]*result[i-1-j]
        return result[n]