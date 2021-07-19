'''
Time Complexity - O(n) (Every element either gets added to stack or gets popped from the stack so O(2n) -> O(n))
Space Complexity - O(n) (stack may have to hold all the elements in the worst case)

The main idea is that there will be subarrays of temperatures which will have a maximum temperature at the end which will be the next warmer day for all the elements in the sub-arrays.
We enumerate the temperatures array from left to right and we keep adding the indexes of temperatures in a stack.
As soon as we encounter a temperature which is more than the temperature of the index stored at the top of the stack, we pop all the indexes from the stack and initialize the output array 
with i-cur i.e. the current (warmer temperature index) - cur (the previous temperatures). We initialize the corresponding index (cur) of the output array (ans).
We then append this maximum value's index in the stack and proceed to further values.

'''
class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans