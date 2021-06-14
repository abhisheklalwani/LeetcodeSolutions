'''
Time Complexity - O(m+n) 
Space Complexity - O(1)
The trick is to start from the largest element rather than shifting all the smaller elements.
We start with 2 pointers (We use m and n only) which start at the end of 2 arrays. (m-1 for nums1 and n-1 for nums2) (Here, end of the array in case of nums1 means the end of relevant numbers and not the 0s).
We then compare the last element of both the arrays and append the larger one at the last index of nums1 (Last inclding the 0s).
We then move the pointer of the selected element to the left and compare the numbers from the 2 arrays again.
We keep doing this till we have exhausted one array.
We then check which array we have exhausted.
If it's nums2, nums1 is remaining which is already sorted in place.
If it's nums1, nums2 is remaining which we then move to nums1, since the desired output is in nums1.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        current_index = -1
        while m>0 and n>0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[current_index] = nums1[m-1]
                m-=1
                current_index-=1
            else:
                nums1[current_index] = nums2[n-1]
                n-=1
                current_index-=1
        if n!=0:
            nums1[:n] = nums2[:n]