'''
Time Complexity - O(n^2)
Space Complexity - O(1) (not counting the output)

The idea is that every time we visit a new index in the matrix we mark it as visited by setting it's value to -101 (range of values in the matrix is -100 to 100).
We start with a directions array which starts with the right direction and then is followed by down, left and up.
The idea is that once we have explored 1 direction fully, we take a right and move to the next direction. So, we first start with right.
Once we reach an invalid index(already visited or matrix bounds), we take a right turn.
We keep doing this until we reach a place where even the right turn results into a visited index.
At this point, we return [-1,-1,-1] from our helper method and use that condition to break the for loop.
We have defined a helper function to return the next valid index based on the current index and the logic mentioned above.
We keep storing every index value in the result array and we return the result array.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        current_direction_index = 0
        current_index = [0,0]
        result = []
        while current_index != [-1,-1]:
            result.append(matrix[current_index[0]][current_index[1]])
            matrix[current_index[0]][current_index[1]] = -101
            output = getNextIndex(matrix,current_direction_index,directions,current_index)
            current_index = [output[0],output[1]]
            current_direction_index = output[2]
        return result

def getNextIndex(matrix,current_direction_index,directions,current_index):
    new_index_x = current_index[0]+directions[current_direction_index][0]
    new_index_y = current_index[1]+directions[current_direction_index][1]
    if isIndexValid(new_index_x,new_index_y,matrix):
        return [new_index_x,new_index_y,current_direction_index]
    else:
        current_direction_index = (current_direction_index+1)%len(directions)
        new_index_x = current_index[0]+directions[current_direction_index][0]
        new_index_y = current_index[1]+directions[current_direction_index][1]
        if isIndexValid(new_index_x,new_index_y,matrix):
            return [new_index_x,new_index_y,current_direction_index]
        else:
            return [-1,-1,-1]

def isIndexValid(new_index_x,new_index_y,matrix):
    if new_index_x < 0 or new_index_x >= len(matrix) or new_index_y < 0 or new_index_y >= len(matrix[0]) or matrix[new_index_x][new_index_y] == -101:
        return False
    return True