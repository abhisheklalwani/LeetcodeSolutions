'''
Time Complexity - O(m*n) (We go through the entire grid twice and once more in the worst case if we have to add all the elements in the bfsQueue)
Space Complexity - O(m*n) (bfsQueue will have to hold all the grid elements in the worst case)

Simple BFS Question.
We first initialize an empty bfsQueue.
Then, we add all the grid elements in the queue which are 2 i.e. the position of all the rotten oranges in the beginning.
We also add 0 with all these elements since that signifies the time corresponding to when they became rotten (In this case 0 since they were
rotten to begin with).
Then, until the queue is empty, we keep popping out the elements.
Once we pop out an element, we check the length of the bfsQueue.
It will be 0 for the last element reachable via BFS.
It can be 0 for other elements too but it will be 0 for sure for the last element reachable via BFS.
The last element reachable via BFS will have the maximum rotting time i.e. the time corresponding to it will be our answer.
We thus save it numMinutes.
The last update to numMinutes will be our answer.
Now, once we have our currentElement popped out, we check for all it's valid neighbors.
If a valid neighbor has a value of 1, we append it to the BFSQueue (with rotting time of the current element + 1) and we make the grid value of the
neighbor as 2. This ensures that we have marked this index as visited and thus we don't need to maintain a separate visited array.
Once we are done with this, we check if there are still any 1s in the grid. If yes, we return -1 since that means there are discrete components in the 
grid and not every compoment has a rotten orange (and thus there is some element which is unreachable).
If there are no 1s in the grid, we simply return numMinutes.
'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        numMinutes = 0
        bfsQueue = []
        m = len(grid)
        n = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bfsQueue.append((0,[i,j]))
        while bfsQueue:
            current_minute, current_index = bfsQueue.pop(0)
            if len(bfsQueue) == 0:
                numMinutes = current_minute       
            for dir in dirs:
                target_index = [current_index[0]+dir[0],current_index[1]+dir[1]]
                if target_index[0] >=0 and target_index[0] < m and target_index[1] >=0 and target_index[1] < n and grid[target_index[0]][target_index[1]] == 1:
                    bfsQueue.append((current_minute+1,target_index))
                    grid[target_index[0]][target_index[1]] = 2
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        else:
            return numMinutes