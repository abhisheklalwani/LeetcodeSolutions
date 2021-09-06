'''
Time Complexity - O(n^2) (Worst case all the elements will be added to the bfs_queue)
Space Complexity - O(n^2) (Worst case all the elements will be added to the visited set)
Simple BFS Question.
You start at the given row and column index and you add it to the bfs_queue and the visited set.
Then, you check all the 4 surrounding valid indexes in the image.
If, in any of the surrounding indexes, you find that the value of image is same as the source row and column and it is not yet in visited,
we add it to the queue and the visited set.
We keep up this loop as long the as the queue is not empty.
As soon as the queue is empty, we break the loop.
Then, for all the indexes in the visited set, we change the color to the newColor.
We finally return the image.
'''
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        bfs_queue = []
        bfs_queue.append((sr,sc))
        visited = set()
        visited.add((sr,sc))
        while bfs_queue:
            current = bfs_queue.pop(0)
            top = (current[0]-1,current[1])
            right = (current[0],current[1]+1)
            bottom = (current[0]+1,current[1])
            left = (current[0],current[1]-1)
            for index in [top,right,bottom,left]:
                if index not in visited and index[0]>=0 and index[0]<len(image) and index[1]>=0 and index[1]<len(image[0]) and image[index[0]][index[1]] == image[current[0]][current[1]]:
                    visited.add(index)
                    bfs_queue.append(index)
        for pixel in visited:
            image[pixel[0]][pixel[1]] = newColor
        return image
                
        
                
        
