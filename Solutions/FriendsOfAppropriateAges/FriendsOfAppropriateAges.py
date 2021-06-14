'''
# Time Complexity - O(n) 
# Space Complexity - O(n)
The trick here is to leverage the range in which all the values of age belong (1 <= ages[i] <= 120).
Once you have created a counter, which keeps count of all the ages in the given array, You can just operate directly on the array using a nested for loop.
Since the range of ages is small, it takes up a worst case constant time of O(120*120).
One thing to note here is that we should always iterate a Counter/dict using items and not the .keys.
.keys method is very expensive in terms of the time taken.
'''
class Solution(object):
    def numFriendRequests(self, ages):
        counter = Counter(ages)
        count = 0
        for k1,v1 in counter.items():
            for k2,v2 in counter.items():
                if k1 >= k2 and k1 < 2*k2-14:
                    count+=v1*v2
                    if k1 == k2:
                        count-=v1         
        return count