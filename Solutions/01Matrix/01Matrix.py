'''
Time Complexity - O(m*n) (Worst case all the entries in the grid can be 1)
Space Complexity - O(m*n) (Worst case all the entries will be added to the visited set)
BFS Question since we are interested in finding the 0 with the least distance from each cell.
The idea is that we add all the 0 elements' indexes in a queue.
We pop out every 0 index from the queue and visit all the valid neighbors of that node.
If the distance of the neighbor (which is maintained in a separate distance matrix initialized as -1) is -1, we initialize
it with distance of current node + 1. (Current being the node which we have popped out from the bfs queue).
This works because in bfs, we visit nodes incrementally.
We start with a 0 node and perform 1 iteration of the bfs.
Since there is a common queue for all the elements undergoing bfs, We incrementally visit all the neighboring elements from all the nodes.
First value to reach a -1 node can be assumed as the minimum distance from the 0 node.
We start with initializing a distance matrix with all the values being -1.
We add all the indexes having value 0 in the original matrix to a queue.
While the queue is not empty, we keep popping elements from the queue and we keep visiting all the valid neighbors of that element.
If the value of neighbor in the distacne matrix is -1, we initialize it distance[current_element]+1.
We keep doing this until the queue is empty.
We finally return the distance matrix.
'''
import collections
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        numRows = len(mat)
        numColumns = len(mat[0])
        distance = [[-1]*numColumns for i in range(numRows)]
        bfsQueue = collections.deque()
        for i in range(numRows):
            for j in range(numColumns):
                if mat[i][j] == 0:
                    distance[i][j]=0
                    bfsQueue.append((i,j))
        while bfsQueue:
            currentRow,currentColumn = bfsQueue.popleft()
            for i,j in directions:
                targetRow,targetColumn = currentRow+i,currentColumn+j
                if targetRow>=0 and targetRow<numRows and targetColumn>=0 and targetColumn<numColumns:
                    if distance[targetRow][targetColumn] == -1:
                        distance[targetRow][targetColumn] = distance[currentRow][currentColumn]+1
                        bfsQueue.append((targetRow,targetColumn))
        return distance