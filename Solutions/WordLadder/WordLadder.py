'''
Time Complexity - O(len(wordList)*len(beginWord)*25) (3 nested loops - while loop will run len(wordList) times in the worst case, rest 2 are for loops of fixed lengths
as seen in the code)
Space Complexity - O(len(beginWord)*len(wordList)) (All the strings will be added to the bfs queue plus the wordSet will also be of the same order)

Since we want the 'shortest' transformation sequence, we perform a BFS traversal.
Our starting node is fixed (beginWord).
We initialize an empty bfsQueue and we add our beginWord to it, along with the the length of the transformation sequence required to reach the word. In this case,
it will just be 1 since we are starting with the said word.
We also create a wordSet from the wordList for faster retreival for elements as we will see in the bfsloop.
Now, while the bfsQueue is not empty, we pop elements from the queue.
If the popped element has the string which we are trying to reach, we return the corresponding lenght of the transformaton sequence (which we just popped from the bfs
queue).
If not, we try generating all the neighbors of the popped word.
Then we search for those neighbors in wordSet.
If we find them in the wordSet, this means they are valid neighbors and thus we append them to the bfsQueue.
We also need to check that these neighbors are not visited already.
For this, everytime we find a valid neighbor in the wordSet, we remove it from the wordSet.
The existence of the the word in the wordSet signifies that the word is not visited already.
Since all the words in the wordSet are unique (as mentioned in the question), we can use wordSet to keep track of the visited word.
We finally return 0 after the while loop since that signifies that there is no valid sequence.

'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        bfsQueue = []
        bfsQueue.append((1,beginWord))
        wordSet = set(wordList)
        while bfsQueue:
            numWords, currentWord = bfsQueue.pop(0)
            if currentWord == endWord:
                return numWords
            for i in range(len(currentWord)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    neighbor = currentWord[:i]+c+currentWord[i+1:]
                    if neighbor in wordSet:
                        wordSet.remove(neighbor)
                        bfsQueue.append((numWords+1,neighbor))
        return 0