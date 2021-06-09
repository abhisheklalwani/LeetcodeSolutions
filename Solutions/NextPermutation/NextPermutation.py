'''
Time Complexity - O(n) 
Space Complexity - O(1)
1. Start from its last element, traverse backward to find the first one with index i that satisfy num[i-1] < num[i]. So, elements from num[i] to num[n-1] is reversely sorted.
2. To find the next permutation, we have to swap some numbers at different positions, to minimize the increased amount, we have to make the highest changed position as high as possible. Notice that index larger than or equal to i is not possible as num[i,n-1] is reversely sorted. So, we want to increase the number at index i-1, clearly, swap it with the smallest number between num[i,n-1] that is larger than num[i-1]. For example, original number is 121543321, we want to swap the '1' at position 2 with '2' at position 7.
3. The last step is to make the remaining higher position part as small as possible, we just have to reversely sort the num[i,n-1]
Think of the example - 121543321
'''
class Solution(object):
    def nextPermutation(self, nums):
        index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            return nums.reverse()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[index]:
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp
                break
        nums[index+1:] = nums[index+1:][::-1]
        return nums