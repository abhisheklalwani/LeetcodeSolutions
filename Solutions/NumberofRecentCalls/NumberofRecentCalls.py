'''
Time Complexity - O(n) 
Space Complexity - O(n)
Here, n represents the number of pings.

We maitain a queue.
At every ping, we eliminate all the entries from the queue which are less than t-3000.
We return the length of queue at the end, to represent the count of valid requests.
'''
class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.pop(0)
        return len(self.queue)