'''
Time Complexity - O(n^2)
Space Complexity - O(1) (not counting the output)

We basically define a helper function to predit the next index given the current index of the ball.
We keep predicting the next index till we reach the end of the matrix or we hit a wall of a 'V' in the path.
At the end, we either return -1 to signify a wall block or a V block and the column index of exit in case the ball passes all the way through.
We call the helper method for every starting index (all the elements of the first row).
In the helper function, there are overall 6 cases - 
1. current_index = +1 and right index == wall -> block
2. current_index = +1 and right index == -1 -> block
3. current_index = +1 and right index == +1 -> flow to bottom right
Same 3 more cases when current_index = -1.
We analyze all these in the helper function and return the next index accordingly.
'''
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(grid[0])):
            current_index = [0,i]
            while current_index[0] != len(grid) and current_index != [-1,-1]:
                current_index = predictNextIndex(grid,current_index)
            if current_index == [-1,-1]:
                result.append(-1)
            else:
                result.append(current_index[1])
        return result

def predictNextIndex(grid,current_index):
    if grid[current_index[0]][current_index[1]] == 1:
        if current_index[1] == len(grid[0])-1 or grid[current_index[0]][current_index[1]+1] == -1:
            return [-1,-1]
        else:
            return [current_index[0]+1,current_index[1]+1]
    if grid[current_index[0]][current_index[1]] == -1:
        if current_index[1] == 0 or grid[current_index[0]][current_index[1]-1] == +1:
            return [-1,-1]
        else:
            return [current_index[0]+1,current_index[1]-1]