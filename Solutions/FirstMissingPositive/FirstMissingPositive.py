'''
# Time Complexity - O(n) 
# Space Complexity - O(1)
Basic idea is that if we have an array of length l, the required missing positive will always be in the range of [1,l+1].
l+1 will happen when you have all the entries of [1,l] in the array.
Now, since we are only concerned about the values between [1,l+1], we ignore all the outside values and set them to 0 in the array.
Note that we append a 0 in the beginning of our solution which makes the value of len(nums) = l+1 which is what we use to eliminate the irrelevant value.
Think of it this way - In an array of length 4, if you appned 0 to it and find a 5 in the array, your answer lies in the range of [1,4] (Since one of them is missing)
and you can safely ignore the value 5. Similarly you can ignore the negative values and 0 too.
Once you have done that, we need to store the occurence of a particular integer in the same array. We use indexes for this.
We take nums[i] and increment the nums[nums[i]] by len(nums).
Now, we also want to make sure that once an index is incremented, the value stored there is not lost.
Thus, we add %len(nums) to amke sure that we update the correct index.
Looking at an example, if the value of 1 is stored at index 4, which then gets incremented by 5 (len(nums)), the value now stored is 6.
But we also want to increment nums[1] since 1 was originally present in the array. Thus we update nums[6%5]=nums[1] by len(nums).
After doing all this, if any index in the array has a value less than len(nums), that signifies that the element corresponding to that index is missing in the array.
We return the same.
A cleaner and more readable solution will be to maintain a separate array for checking the occurence of integers in the required range.
But the problem specifies to use O(1) space thus this solution.
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] >= len(nums) or nums[i] <= 0:
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i]%len(nums)] += len(nums)
        for i in range(1,len(nums)):
                if nums[i] < len(nums): 
                    return i
        return len(nums)