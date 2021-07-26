'''
Time Complexity - O(n^2) (Worst case all the entries in the grid can be 1)
Space Complexity - O(n^2) (Worst case all the entries will be added to the visited set)
Simple DFS Question.
We start visiting all the elements of the grid in a sequential order.
If it is already not in visited and if it is 1, we add the index to the visited set and start a recursive DFS from the index.
We check if the surrounding 4 indexes are valid and if the (row,column) pair is not in visited and if the surrounding index is '1'.
If all the conditions hold true, We call the DFS function with the surroundnig index.
The idea is that once you have completed a DFS from a given index, it is counted as an island and we can thus inrement the count of Islands.
Since we are traversing the entire grid, we can be sure that we have covered all the islands.
Since we are mainting the visited set, we can be sure that we will not visit any island twice.
We finally return the numIslands.
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def DFSUtil(row,column,grid,visited):
            visited.add((row,column))
            if row-1>=0 and row-1<len(grid) and column>=0 and column<len(grid[0]) and grid[row-1][column]=='1' and (row-1,column) not in visited:
                DFSUtil(row-1,column,grid,visited)
            if row>=0 and row<len(grid) and column-1>=0 and column-1<len(grid[0]) and grid[row][column-1]=='1' and (row,column-1) not in visited:
                DFSUtil(row,column-1,grid,visited)
            if row+1>=0 and row+1<len(grid) and column>=0 and column<len(grid[0]) and grid[row+1][column]=='1' and (row+1,column) not in visited:
                DFSUtil(row+1,column,grid,visited)
            if row>=0 and row<len(grid) and column+1>=0 and column+1<len(grid[0]) and grid[row][column+1]=='1' and (row,column+1) not in visited:
                DFSUtil(row,column+1,grid,visited) 
        numRows = len(grid)
        numColumns = len(grid[0])
        visited = set()
        numIslands = 0
        for i in range(numRows):
            for j in range(numColumns):
                if (i,j) not in visited and grid[i][j]=='1':
                    DFSUtil(i,j,grid,visited)
                    numIslands +=1
        return numIslands
        
            
        
                
        
                
        