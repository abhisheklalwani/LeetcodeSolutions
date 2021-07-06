'''
Time Complexity - O(m*n*(4^s)) (4 calls every function which is repeated s times where s = len(word), the process is repeated m*n times where m and n are dimensions of the board).
Space Complexity - O(1) (all in-place modifications)

We first check the validity of the index which we are about to analyze.
The index should point to valid element in the board and should not be already visited in the string which we are trying to construct. Think about [A,B,C,D]
and how ABCB is not a valid string since you can't visit B again. To prevent this, we maintain a set() called visited.
Once we have establised that index is valid, we compare the character in the board which we are visiting right now.
If current_string + current_character (on the board) is the starting of the string then our current character is valid and we append it to our current_string:
    We also add the current index to the visited set to make sure that we don't count this index again.
    Then we compare current_string to the word.
    If they are equal we return True (Our Break condition)
    If not, we check the surrounding 4 indexes for the next character.
    If any one of the is True, we return True (basically propagate it back).
    If they are all False, we return False back.
    We also remove the current index from visited and remove the current character from the current string since this character might be a neighbor of a character
    which we might visit later and might be a valid character then.
    Think about [["a","b"],["c","d"]] and "cdba". We don't want a to be in visited when we come at a from b after d.
else:
    We return False.
We do this for all the indexes in the board.
'''
class Solution(object):
    def exist(self, board, word):
        def backtrack(currentString, word, board, rowIndex, columnIndex, visited):
            if (rowIndex,columnIndex) in visited or rowIndex < 0 or rowIndex >= len(board) or columnIndex < 0 or columnIndex >= len(board[0]):
                return False
            if word[len(currentString)] == board[rowIndex][columnIndex]:
                currentString += board[rowIndex][columnIndex]
                visited.add((rowIndex,columnIndex))
                if currentString == word:
                    return True
                else:
                    if (
                        backtrack(currentString, word, board, rowIndex-1, columnIndex,visited) or 
                        backtrack(currentString, word, board, rowIndex, columnIndex-1,visited) or 
                        backtrack(currentString, word, board, rowIndex+1, columnIndex,visited) or 
                        backtrack(currentString, word, board, rowIndex, columnIndex+1,visited)):
                        return True
                    else:
                        currentString = currentString[:-1]
                        visited.remove((rowIndex,columnIndex))
                        return False
            else:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if backtrack('',word, board, i, j,visited):
                    return True
        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """