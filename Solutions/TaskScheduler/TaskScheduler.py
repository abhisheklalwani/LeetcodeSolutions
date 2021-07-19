'''
Time Complexity - O(n)
Space Complexity - O(n)

The main idea behind this question is that we will compare the length of the string formed by using all the unique characters once with the value of n-1.
This is because in theory the minimum time will be observed when we try to spread all the tasks out as much as possible.
In case of ['A','B','C','A','B','C'], the ideal combination will be A->B->C->A->B->C (Ignoring n for a second). Anything other than this will take more time
since atleast one set of same task will be next to each other or atleast closer to each other.
Now let's take a look at example and see how it will be done.
[A,A,A,A,A,B,B,B,B,C,C,C,D,D,E] and n=4.
Now, based upon the idea mentioned above, the series will be (wihout idle timeouts for now).
A -> B -> C -> D -> E
A -> B -> C -> D (   )
A -> B -> C (        )
A -> B (             )
A (                  )
For any combination, we can visualize the series to be similar in nature, where we first arrange the unique letters once and then we go down the filling the
remaining letters.
Now as you can see there is empty space as specified by the brackets above which will be filled with idle timeouts depending upon the value of n.
If the value of n is less than the length of the string, we add no idle timeouts and direct start the next string.
If the value of n is more than the length of the string, we add enough idle timeouts to start the 'A' process again (n-(len(string)-1)).
This means that the length of the strings in the final order should be n+1 (with or without idle timeouts).
And the total number of strings will be maximum of all the values of tasks (5 in the above example).
The only thing is that there won't be idle timeouts at the end of the last string (A in the above example).
So we need to remove them. We do this by adding only the count of maximum occurence for the last row (1 in above example since 5 only occurs once).
So our overall formula becomes width*height+max_count where
max_count is count of maximum value in the counter values.
height is max(values)-1 (since we don't add idle timeout in the last row).
Width is n+1.
The solution for the above problem then becomes - 
A -> B -> C -> D -> E ->
A -> B -> C -> D -> idle -> 
A -> B -> C -> idle -> idle->
A -> B ->idle -> idle -> idle->
A
5*4+1 = 21
We also place a check in the end for special cases like n=0 where we make sure that we don't return which is less than the total number of tasks itself.
If that happens we just return len(tasks) since that will be the minimum time it takes for the tasks to complete.
'''
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        values = counter.values()
        width = n+1
        height = max(values)-1
        total = width*height + values.count(height+1)
        return max(total,len(tasks))