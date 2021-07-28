'''
Time Complexity - O(V+E) (Simple DFS traveral using adjacency list, would have been O(v^2) if the representation was via an adjacency matrix)
Space Complexity - O(V) (All the vertices will be added to the visited set)
The main idea is that during a DFS traversal of an undirected graph, if we visit a node that is already visited and is not the parent of 
the node, then there is a cycle in the graph.
We start with initializing an empty visited set.
We then start by performing DFS on every non-visited vertex.
This is done to ensure that we cover all the disjoint components of the graph.
Then, in the recursive function, we add the current node to the visited set and then we iterate through all the neighbors of the current node.
If any neighbor is not visited, we call the DFSUtil function on that node with the parent as the current node. If that returns True, we propogate
that True higher in the recursion stack.
If the neighbor is already visited, we check if the neighbor is parent.
If not, we return True since that signifies the cycle.
At the end of visiting all the neighbors, we return False since no Cycle has been found.
'''
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		def DFSUtil(vertex,visited,parent):
		    visited.add(vertex)
		    for neighbor in adj[vertex]:
		        if neighbor not in visited:
		            if DFSUtil(neighbor,visited,vertex):
		                return True
		        else:
		            if neighbor != parent:
		                return True
		    return False
		visited = set()
		for i in range(V):
		    if i not in visited:
		        if DFSUtil(i,visited,-1):
		            return True
		return False