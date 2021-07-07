'''
Time Complexity - O(n^3) (You generate all possible combinations of the starting numbers (n^2) and check whether they result upto a valid sequence (n)).
Space Complexity - O(2+log(n)) = O(log(n)) (2 stacks to determine the various combinations of output numbers and log(n) to compare the various substrings. O(1)
for every stack).


First we check if we have 2 valid numbers to generate the next number.
If yes, we generate the next number and compare the beginning of the string with the next number. 
If they are equal, We call backtrack again with the reduced string and the new 2 numbers. '35' and [1,2] -> '5' with [2,3]
If they are not equal, we return False.
If we have only 1 valid number, we try and extract one more from the remaining string and call the baktrack function with the update remainingString and the 2
valid numbers.
If we have no valid numbers, we try and extract one valid number from the remaining string call the baktrack function with the update remainingString and 1
valid number.
In both the cases we check that the valid numbers should not have leading zeros (first == 0 and last=i-1 => !=0, could have used startsWith too but it gave an error for 101).
'''
class Solution(object):
    def isAdditiveNumber(self, num):
        def backtrack(remainingString,currentNumbers):
            if len(remainingString) == 0:
                return True
            else:
                if len(currentNumbers) == 2:
                    nextNumber = sum(currentNumbers)
                    if remainingString[:len(str(nextNumber))] == str(nextNumber):
                        currentNumbers[0] = currentNumbers[1]
                        currentNumbers[1] = nextNumber
                        return backtrack(remainingString[len(str(nextNumber)):],currentNumbers)
                    else:
                        return False
                else:
                    if len(currentNumbers) == 1:
                        for i in range(1,len(remainingString)):
                            if remainingString[0] == '0' and remainingString[i-1] != '0':
                                continue
                            if backtrack(remainingString[i:],currentNumbers+[int(remainingString[:i])]):
                                return True
                        return False
                    else:
                        for i in range(1,len(remainingString)):
                            if remainingString[0] == '0' and remainingString[i-1] != '0':
                                continue
                            if backtrack(remainingString[i:],currentNumbers+[int(remainingString[:i])]):
                                return True
                        return False
        return backtrack(num,[])