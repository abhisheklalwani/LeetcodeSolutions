'''
Time Complexity - O(n) (Here n represent the number of nodes in the tree)
Space Complexity - O(n) (worst case all the nodes will have a separate column index and thus seprate keys in the dict)

The main result required is the grouping of the node values on the basis of column values.
Once that grouping is done, we sort all the nodes at a given column index based upon 2 indexes.
1. Using the row index
2. Using the values of the nodes
We use a dictionary to help us with the grouping.
We iterate through the entire tree and append all the node values and the row index at the appropriate key in the dictionary.
Once the dictionary is made, we sort all the keys in the dictionary.
Then, for every key, we sort the stored array based upon 2 keys as specified above.
We finally append all the results to an array and return it.

'''
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = {}
        def util(root,row,col,result):
            if col in result:
                result[col].append([row,root.val])
            else:
                result[col] = [[row,root.val]]
            if root.left:
                util(root.left,row+1,col-1,result)
            if root.right:
                util(root.right,row+1,col+1,result)
        util(root,0,0,result)
        final_result = []
        for i in sorted(result.keys()):
            temp = sorted(result[i],key = lambda x:(x[0],x[1]))
            temp = [i[1] for i in temp]
            final_result.append(temp)
        return final_result