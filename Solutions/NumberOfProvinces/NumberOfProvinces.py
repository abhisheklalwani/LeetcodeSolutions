'''
Time Complexity - O(n^2) (Since we will be using DFS and the graph is represented as an adjacency matrix).
Space Complexity - O(n) (All the vertices will get added to the visited set).
Simple DFS Question.
We initialize an empty visited set.
We iterate through all the cities and perform a DFS from every unvisited node.
At the end of this DFS, we increment the province counter.
In the DFS function, we add the current node to the visited set and we call DFS funcion recursively on all the un-visited neighbors.
We finally return the province counter.
'''
class Solution(object):
    def findCircleNum(self, isConnected):
        def DFSUtil(city,visited,isConnected):
            visited.add(city)
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor]==1 and neighbor not in visited:
                    DFSUtil(neighbor,visited,isConnected)
        
        numRows = len(isConnected)
        visited = set()
        numProvinces = 0
        for city in range(numRows):
            if city not in visited:
                DFSUtil(city,visited,isConnected)
                numProvinces+=1
        return numProvinces     