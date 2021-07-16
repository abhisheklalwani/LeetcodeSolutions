'''
Time Complexity - O(V) (Here V represents the number of vertices in the graph, which in our case reprsents all the intermediate and the target combination)
Space Complexity - O(V) (Think about a tree where there is one root node and all the subsequent node are at the next level. In such a case, we have to store V-1 vertices in the stack which is O(V).
In worst case we might have to store all the vertices in the stack, which leads to V).

We solve this problem using BFS.
We start at 0000 which becomes our starting node. 
We add it to the visited set.
Our nodes comprise of 2 entities - 
1. The code number
2. Number of steps required to reach the corresponding code number
We start by adding (0000,0) to our queue.
Then, while the queue is non-Empty, we pop out the first element of the queue, analyze it and add all the neighbors of the node at the end of the queue.
The analyzing will depend on the problem statement.
In our case, we check if the current node (the one which we just popped out) is equal to the target.
If yes, we return the corresponding number of steps.
We also check if the current node is in the deadend set.
If yes, we just continue the loop (ignore the subsequent nodes of that branch).
If not, we calculate all the neighbors of the current node.
We do that by going 1 ahead and 1 back on all the 4 dials.
We generate the new sequence depending on the dial and the move and we add it to the stack along with steps+1.
We return -1 finally if the required target node is not reachable from the source node.
'''
class Solution(object):
    def openLock(self, deadends, target):
        queue = []
        queue.append(('0000',0))
        visited = set('0000')
        dead_set = set(deadends)
        while len(queue):
            current,steps = queue.pop(0)
            if current == target:
                return steps
            if current in dead_set:
                continue
            for i in range(4):
                for move in [-1,+1]:
                    new_digit = str((int(current[i])+move)%10)
                    new_sequence = current[:i]+new_digit+current[i+1:] 
                    if new_sequence not in visited:
                        visited.add(new_sequence)
                        queue.append((current[:i]+new_digit+current[i+1:],steps+1))
        return -1
        