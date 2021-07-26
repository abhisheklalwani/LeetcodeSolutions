'''
Time Complexity - O(V+E) (Same as DFS, V can be the number of courses and E can be the number of pre-req conditions)
Space Complexity - O(V) (Length of the visited array)
The main idea is to find a cycle in a directed graph.
We do that by maintaing a recursion stack.
If a node which we are currently visiting exists in the recursion stack already, we can say that we have found a cycle and we can return False.
In the code, we first make the adjacency list by iterating through the prerequisite array.
We also intialize an array of zeros called visited which we use to keep track of the visited nodes.
Once we have done that, we call DFS on every node.
A value of -1 in the visited array signifies that the current index is in the recursion stack.
A value of 1 in the visited array signifies that the current index is already visited and popped out of the recursion stack.
A value of 0 in the visited array signifies that the current index is unvisited.
As we enter the DFSUtil method, we check if the value of visted at the current element is -1.
That signfies a cycle, so we return False (course schedule not possible).
If the value is 1, we just return True (course schedule is possible).
If the value is 0, we set the value to -1 (add it to the recursion stack) and call DFSUtil on all the neighbors.
If any neighbor returns False, we also return False since that signifies a cycle at one of the neighbors and we need to propagate it back.
Finally, once we are done visiting all the neighbors we pop the current element out the recursion stack by setting it's value equal to 1, signifying that
this node is visited and no cycles were found.
We finally return True signifying that no cycles were found at this node.
We do this for all nodes in the list and see if any node returns False.
If yes, we also return False.
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def DFSUtil(adjacency_list,current,visited):
            if visited[current] == -1:
                return False
            if visited[current] == 1:
                return True
            visited[current] = -1
            for neighbor in adjacency_list[current]:
                if not DFSUtil(adjacency_list,neighbor,visited):
                    return False
            visited[current] = 1
            return True

        adjacency_list = {i:[] for i in range(numCourses)}
        visited = [0]*numCourses
        for prereq in prerequisites:
            adjacency_list[prereq[1]].append(prereq[0])
        for i in range(numCourses):
            if not DFSUtil(adjacency_list,i,visited):
                return False
        return True
        
        
                
                
        
        
        
        
            
        
                
        
                
        