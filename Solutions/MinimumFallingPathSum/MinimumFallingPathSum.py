'''
Time Complexity - O(n*n) (m-> number of coins,n->amount)
Space Complexity - O(1)
We start at the second row and go through each element.
At each element, we check all its valid parents.
According to the question, it includes the element directly above the current element, combined with the diagnolly upward elements, assuming they are valid indexes.
So as you can see in the code, we first initialize the minParents array corresponding to the current index (i,j) by directly including the element just above the
current element since that will always be a valid index and thus a valid element.
Then, if the diagonally upward left index (i-1,j) is a valid index, we will include that in our minParents array.
Similary, we extract the upward right index as well if it is a valid index.
Finally, we increment the current index value by the minium of all tha parents.
We finally return the minimum value in the last row.  
'''
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        for i in range(1,n):
            for j in range(n):
                minParents = [matrix[i-1][j]]
                if j-1 >= 0:
                    minParents.append(matrix[i-1][j-1])
                if j+1 < n:
                    minParents.append(matrix[i-1][j+1])
                matrix[i][j] +=  min(minParents)
        return min(matrix[-1])
        