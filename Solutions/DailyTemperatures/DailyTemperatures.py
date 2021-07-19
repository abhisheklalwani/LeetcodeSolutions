'''
Time Complexity - O(n) (Even though the number of steps to jump (while loop) is NOT a constant, 
note that each element in a 'valley' will be accessed at most twice thanks to the leaps (consider the example T=[5,4,5,1,2,3,4,6]), 
the algorithm essentially only keeps the monotonely increasing part of the original sequence. Thus the complexity is O(n).
https://leetcode.com/problems/daily-temperatures/discuss/397728/Easy-Python-O(n)-time-O(1)-space-beat-99.9)
Space Complexity - O(1) (not counting the output)

We initialize an array with 0s of length temperatures, and we call it warmer.
We eventually intend to return warmer.
The idea is that we iterate the array from right to left.
We keep track of right_max (maximum value while iterating from the right).
If the current value is greater than right_max, we don't edit warmer and we leave it at 0, since there is no other day in the future where the temperature
is greater than the current_temperature.
If the current value is less than right_max, we check the immediate value to the right.
If it is greater than the current temperature, we initialize the current value of warmer to 1, since only after 1 day a higher temperature will be observed.
If not, then we observe how many days it will take to reach a warmer temperature than the next day (immediate next day to the right) (that day will i + 1 +warmer[i+1]).
We observe the temperature on that day and if it is still less than the current temperature, we observer the next warmer day i.e. the day which will observe a warmer
temperature than i+1+warmer[i+1]. We do this by updating warmer_next continuously.
warmer_next is initialized with 1+warmer[i+1].
warmer_next is updated by adding warmer[i+warmer_next] to the previous value of warmer_next.
As soon as temperatures[i+warmer_next] is greater than temperatures[i], we initialize warmer[i] with warmer_next.
We eventually return warmer.

'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        warmer = [0]*len(temperatures)
        right_max = float('-inf')
        for i in range(len(temperatures)-1,-1,-1):
            if temperatures[i] >= right_max:
                right_max = temperatures[i]
            else:
                if temperatures[i+1] > temperatures[i]:
                    warmer[i] = 1
                else:
                    warmer_next= 1+warmer[i+1]
                    while temperatures[i+warmer_next] <= temperatures[i]:
                        warmer_next += warmer[i+warmer_next]
                    warmer[i] = warmer_next
        return warmer